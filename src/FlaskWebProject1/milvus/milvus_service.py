from unittest import result
from numpy import array, ndarray, expand_dims
from pymilvus import Collection, CollectionSchema, utility, connections
from typing import Optional, Any, Dict
from milvus.constants import (
    DEFAULT_METRIC_TYPE,
    ID_FIELD,
    EMBEDDING_FIELD,
    DYNAMIC_FIELD,
    OPENAI_EMBEDDING_VECTOR_SIZE,
    CollectionSchemaOwner,
)


from milvus.fields.qna_fields import (
    CHUNK_CONTENT_FIELD,
    create_field_schemas as create_qna_field_schema,
    SEARCHABLE_FIELD as QNA_SEARCHABLE_FIELD,
    VERSION_STATUS_FIELD as QNA_VERSION_STATUS_FIELD,
    BOOK_ID_FIELD as QNA_BOOK_ID_FIELD,
    CATEGORY_FIELD as QNA_CATEGORY_FIELD,
    OUTPUT_FIELDS_WITH_EMBEDDING as QNA_OUTPUT_FIELDS_WITH_EMBEDDING,
    OUTPUT_FIELDS_WITH_OUT_EMBEDDING as QNA_OUTPUT_FIELDS_WITH_OUT_EMBEDDING,
)
from milvus.fields.search_fields import (
    create_field_schemas as create_search_field_schema,
    SEARCHABLE_FIELD as SEARCH_SEARCHABLE_FIELD,
    VERSION_STATUS_FIELD as SEARCH_VERSION_STATUS_FIELD,
    BOOK_ID_FIELD as SEARCH_BOOK_ID_FIELD,
    CATEGORY_FIELD as SEARCH_CATEGORY_FIELD,
    OUTPUT_FIELDS_WITH_EMBEDDING as SEARCH_OUTPUT_FIELDS_WITH_EMBEDDING,
    OUTPUT_FIELDS_WITH_OUT_EMBEDDING as SEARCH_OUTPUT_FIELDS_WITH_OUT_EMBEDDING,
)
from milvus.fields.faq_fields import (
    create_field_schemas as create_faq_field_schema,
    SEARCHABLE_FIELD as SEARCH_SEARCHABLE_FIELD,
    BOOK_ID_FIELD as SEARCH_BOOK_ID_FIELD,
)

from milvus.models.memory_record import MemoryRecord
from milvus.models.qna_memory_record import QnaMemoryRecord
from milvus.models.search_memory_record import SearchMemoryRecord

# 索引参数
_INDEX_TYPE = "IVF_FLAT"
_NLIST = 1024
_INDEX_NAME = "embedding_index"

# 打个比方 ivf索引就像是把一所小学的小学生分班管理，nlist就是班级数量，假设我们按年龄大小分成nlist个班级，你查询时的nprobe是要查找的班级
# 你要找的人大约有12岁，所以就从高年级里选出nprobe个班，然后你又加了个查询条件“我要找名字叫李明的小朋友”
# 如果那nprobe个班级里没有叫“李明”的小盆友，那就查不到了
# 如果你把nprobe设成nlist的值，相当于全校搜索，那就能查出来了，他可能在一年级的某个班里


def memory_record_to_milvus_dict(
    owner: CollectionSchemaOwner, record: MemoryRecord
) -> dict[str, Any]:
    ret_dict = {}

    concrete_record = {}

    if CollectionSchemaOwner.is_qna(owner):
        concrete_record = record.to_qna_memory_record()
    elif CollectionSchemaOwner.is_search(owner):
        concrete_record = record.to_search_memory_record()
    else:
        raise ValueError("Unsupported schema owner.")

    for key, value in vars(concrete_record).items():
        if value is not None:
            ret_dict[key] = value
    return ret_dict


def milvus_dict_to_memoryrecord(milvus_dict: dict[str, Any]) -> MemoryRecord:
    embedding = milvus_dict.get(EMBEDDING_FIELD)
    if embedding is not None:
        embedding = array(embedding)
    return MemoryRecord(
        id=milvus_dict.get(ID_FIELD),
        text=milvus_dict.get(CHUNK_CONTENT_FIELD),
        embedding=embedding,
        meta=milvus_dict.get(DYNAMIC_FIELD),
    )


def create_expression(field_name: str, values: list[str], operator: str = "in"):
    if values is None or len(values) == 0:
        return ""
    return f"{field_name} {operator} {values}"


# Qna必选表达式
QNA_REQUIRED_EXPRESSION = [
    create_expression(QNA_SEARCHABLE_FIELD, "true", "=="),
    create_expression(QNA_VERSION_STATUS_FIELD, '"Active"', "=="),
]

# Search必选表达式
SEARCH_REQUIRED_EXPRESSION = [
    create_expression(SEARCH_SEARCHABLE_FIELD, "true", "=="),
    create_expression(SEARCH_VERSION_STATUS_FIELD, '"Active"', "=="),
]


def generate_qna_expression(
    ids: Optional[list[str]] = None,
    book_ids: Optional[list[str]] = None,
    categories: Optional[list[str]] = None,
) -> str:
    if ids is None:
        ids = []
    if book_ids is None:
        book_ids = []
    if categories is None:
        categories = []

    qna_id_expression = create_expression(ID_FIELD, ids)
    qna_book_id_expression = create_expression(QNA_BOOK_ID_FIELD, book_ids)
    qna_category_expression = create_expression(QNA_CATEGORY_FIELD, categories)

    expressions = [
        qna_id_expression,
        qna_book_id_expression,
        qna_category_expression,
    ] + QNA_REQUIRED_EXPRESSION

    final_expressions = [expr for expr in expressions if expr]

    return " && ".join(final_expressions)


def generate_search_expression(
    ids: Optional[list[str]] = None,
    book_ids: Optional[list[str]] = None,
    categories: Optional[list[str]] = None,
) -> str:
    if ids is None:
        ids = []
    if book_ids is None:
        book_ids = []
    if categories is None:
        categories = []

    search_id_expression = create_expression(ID_FIELD, ids)
    search_book_id_expression = create_expression(SEARCH_BOOK_ID_FIELD, book_ids)
    search_category_expression = create_expression(SEARCH_CATEGORY_FIELD, categories)

    expressions = [
        search_id_expression,
        search_book_id_expression,
        search_category_expression,
    ] + SEARCH_REQUIRED_EXPRESSION

    final_expressions = [expr for expr in expressions if expr]
    return " && ".join(final_expressions)


def generate_expression(
    owner: CollectionSchemaOwner,
    ids: Optional[list[str]] = None,
    book_ids: Optional[list[str]] = None,
    categories: Optional[list[str]] = None,
):
    if CollectionSchemaOwner.is_qna(owner):
        return generate_qna_expression(ids, book_ids, categories)
    elif CollectionSchemaOwner.is_search():
        return generate_search_expression(ids, book_ids, categories)
    else:
        return ""


def get_output_fields(owner: CollectionSchemaOwner, with_embeddings: bool) -> list[str]:
    if CollectionSchemaOwner.is_qna(owner):
        if with_embeddings:
            return QNA_OUTPUT_FIELDS_WITH_EMBEDDING
        else:
            return QNA_OUTPUT_FIELDS_WITH_OUT_EMBEDDING
    elif CollectionSchemaOwner.is_search(owner):
        if with_embeddings:
            return SEARCH_OUTPUT_FIELDS_WITH_EMBEDDING
        else:
            return SEARCH_OUTPUT_FIELDS_WITH_OUT_EMBEDDING
    else:
        raise ValueError("Unsupported schema owner.")


class MilvusService:
    def __init__(
        self,
        host: str = "localhost",
        port: int = 19530,
        user: str | None = None,
        password: str | None = None,
        timeout: Optional[float] = None,
    ) -> None:
        connections.connect(
            "default", user=user, password=password, host=host, port=port
        )

    def create_collection(
        self,
        owner: CollectionSchemaOwner,
        collection_name: str,
        dimension: int = OPENAI_EMBEDDING_VECTOR_SIZE,
        metric_type: str | None = DEFAULT_METRIC_TYPE,
        overwrite: bool = False,
        consistency: str = "Session",
    ):
        """创建指定Owner的Milvus Collection

        Args:
            collection_name (str): Collection的名称
            dimension (int, optional): Embedding的数组长度，默认是 1536
            metric_type (str, optional): 相似性的度量，默认是 COSINE
            overwrite (bool, optional): 是否覆盖现有的同名Collection，默认是 False
            consistency (str, optional): Milvus操作的一致性级别，包括Strong,Session,Bounded,Eventually。默认是 Session
        """
        schema = self._get_schema_by_owner(owner=owner, dimension=dimension)

        index_param = {
            "index_type": _INDEX_TYPE,
            "params": {"nlist": _NLIST},
            "metric_type": metric_type,
        }

        if utility.has_collection(collection_name=collection_name) and overwrite:
            utility.drop_collection(collection_name=collection_name)

        collection = Collection(
            name=collection_name, schema=schema, consistency_level=consistency
        )

        collection.create_index(
            EMBEDDING_FIELD, index_params=index_param, index_name=_INDEX_NAME
        )

    def get_collections(self) -> list[str]:
        """获取当前的所有的Milvus Collection

        Returs:
            List[str]: Milvus Collection名称集合
        """
        return utility.list_collections()

    def delete_collection(
        self, collection_name: str | None = None, all: bool = False
    ) -> None:
        """删除指定的Milvus Collection

        如果all=True，所有的Collection都会被删除

        Args:
            collection_name (str): 需要删除的Collection的名称
            all (bool, optional): 是否删除所有Collection，默认是 False.
        """
        if collection_name and utility.has_collection(collection_name=collection_name):
            utility.drop_collection(collection_name=collection_name)
            return
        if all:
            for collection in utility.list_collections():
                utility.drop_collection(collection_name=collection)
            self.collections = []

    def check_collection_exist(self, collection_name: str) -> bool:
        """检查指定的Collection是否存在

        Args:
            collection_name (str): 需要检查的Collection的名称

        Returns:
            bool: 如果存在返回True，否则返回False
        """
        return utility.has_collection(collection_name=collection_name)

    def upsert_batch(
        self,
        owner: CollectionSchemaOwner,
        collection_name: str,
        records: list[MemoryRecord],
    ) -> list[str]:
        """新增/修改Entities.

        Args:
            collection_name (str): Collection的名称
            records (bool): 新增/修改的数据

        Returns:
            list[str]: 新增/修改的数据的Id
        """
        if collection_name not in utility.list_collections():
            raise SystemError(
                f"Collection {collection_name} does not exist, cannot upsert."
            )

        data_list = [memory_record_to_milvus_dict(owner, record) for record in records]

        collection = Collection(collection_name)
        ids = collection.upsert(data=data_list).primary_keys
        collection.flush()

        return [str(item) for item in ids]

    def get(
        self,
        owner: CollectionSchemaOwner,
        collection_name: str,
        id: str,
        with_embedding: bool,
    ) -> MemoryRecord:
        """获取指定id的Entity

        Args:
            collection_name (str): Collection的名称
            id (str): 需要获取的id
            with_embedding (bool): 结果中是否包含embedding

        Returns:
            MemoryRecord: id对应的MemoryRecord
        """
        result = self.get_batch(
            owner=owner,
            collection_name=collection_name,
            ids=[id],
            with_embeddings=with_embedding,
        )
        return result[0]

    def get_batch(
        self,
        owner: CollectionSchemaOwner,
        collection_name: str,
        ids: list[str],
        with_embeddings: bool,
    ) -> list[MemoryRecord]:
        """获取指定id的Entity

        Args:
            collection_name (str): Collection的名称
            ids (list[str]): 需要获取的id
            with_embedding (bool): 结果中是否包含embedding

        Returns:
            list[MemoryRecord]: id对应的MemoryRecord
        """
        if not utility.has_collection(collection_name):
            raise Exception(f"Collection {collection_name} does not exist, cannot get.")

        collection = Collection(collection_name)
        collection.load()

        id_expression = create_expression(ID_FIELD, ids)

        result = collection.query(
            expr=id_expression, output_fields=get_output_fields(owner, with_embeddings)
        )

        return [milvus_dict_to_memoryrecord(get) for get in result]

    def delete(self, collection_name: str, id: str) -> None:
        """删除指定id的数据

        Args:
            collection_name (str): Collection的名称
            id (str): 要删除的id
        """
        self.delete_batch(collection_name=collection_name, ids=[id])

    def delete_batch(self, collection_name: str, ids: list[str]) -> None:
        """删除指定id的数据

        Args:
            collection_name (str): Collection的名称
            ids (list[str]): 要删除的id
        """
        if collection_name not in utility.list_collections():
            raise Exception(
                f"Collection {collection_name} does not exist, cannot remove."
            )
        collection = Collection(collection_name)
        collection.load()

        id_expression = create_expression(ID_FIELD, ids)

        result = collection.delete(expr=id_expression)

        collection.flush()

        if result.delete_count != len(ids):
            raise Exception(
                f"Failed to remove all keys, {result.delete_count} removed out of {len(ids)}"
            )

    def search(
        self,
        owner: CollectionSchemaOwner,
        collection_name: str,
        embedding: ndarray,
        limit: int,
        min_relevance_score: float = 0.0,
        with_embeddings: bool = False,
        ids: Optional[list[str]] = None,
        book_ids: Optional[list[str]] = None,
        categories: Optional[list[str]] = None,
    ) -> list[tuple[MemoryRecord, float]]:
        """搜索与embedding最相近的limit条的记录

        Args:
            collection_name (str): Collection的名称
            embedding (ndarray): 搜索的向量
            limit (int):返回的结果数
            min_relevance_score (float, optional): 相关性分数阈值
            with_embeddings (bool, optional): 搜索结果是否包含embedding，默认是False
            ids (list[str], optional): 需要过滤的数据的id
            book_ids (list[str], optional): 需要过滤的数据的book_id
            categories (list[str], optional): 需要过滤的数据的category

        Returns:
            List[Tuple[MemoryRecord, float]]: MemoryRecord和得分元组.
        """

        if collection_name not in utility.list_collections():
            raise Exception(
                f"Collection {collection_name} does not exist, cannot search."
            )

        if len(embedding.shape) == 1:
            embedding = expand_dims(embedding, axis=0)

        collection = Collection(collection_name)

        collection.load()
        metric = collection.index(index_name=_INDEX_NAME).params["metric_type"]

        results = collection.search(
            data=embedding,
            anns_field=EMBEDDING_FIELD,
            limit=limit,
            output_fields=get_output_fields(owner, with_embeddings),
            param={"metric_type": metric},
            expr=generate_expression(owner, ids, book_ids, categories),
        )[0]

        # TODO JSON Serialize
        return [
            (milvus_dict_to_memoryrecord(result.fields), result.distance)
            for result in results
            if result.distance >= min_relevance_score
        ]

    def _get_schema_by_owner(
        self, owner: CollectionSchemaOwner, dimension: int
    ) -> CollectionSchema:
        if CollectionSchemaOwner.is_qna(owner):
            return CollectionSchema(
                create_qna_field_schema(dimensions=dimension), enable_dynamic_field=True
            )
        elif CollectionSchemaOwner.is_search(owner):
            return CollectionSchema(
                create_search_field_schema(dimensions=dimension),
                enable_dynamic_field=True,
            )
        elif CollectionSchemaOwner.is_faq(owner):
            return CollectionSchema(
                create_faq_field_schema(dimensions=dimension), enable_dynamic_field=True
            )
        else:
            raise ValueError("Unsupported schema owner.")

    def _get_qna_memory_records(
        memory_records: list[MemoryRecord],
    ) -> list[QnaMemoryRecord]:
        qna_memory_records = []
        for memory_record in memory_records:
            qna_memory_record = memory_record.to_qna_memory_record()
            if qna_memory_record is not None:
                qna_memory_records.append(qna_memory_record)
        return qna_memory_records

    def _get_search_memory_records(
        memory_records: list[MemoryRecord],
    ) -> list[SearchMemoryRecord]:
        search_memory_records = []
        for memory_record in memory_records:
            search_memory_record = memory_record.to_search_memory_record()
            if search_memory_record is not None:
                search_memory_records.append(search_memory_record)
        return search_memory_record
