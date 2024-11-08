from pymilvus import Collection, CollectionSchema, utility, connections
from typing import Optional, Any, Dict
from milvus.constants import (
    DEFAULT_METRIC_TYPE,
    EMBEDDING_FIELD,
    OPENAI_EMBEDDING_VECTOR_SIZE,
    CollectionSchemaOwner,
)
from milvus.fields.qna_fields import create_field_schemas as create_qna_field_schema
from milvus.fields.search_fields import (
    create_field_schemas as create_search_field_schema,
)
from milvus.fields.faq_fields import create_field_schemas as create_faq_field_schema
from milvus.models.memory_record import MemoryRecord
from milvus.models.qna_memory_record import QnaMemoryRecord
from milvus.models.search_memory_record import SearchMemoryRecord

# 索引参数
_INDEX_TYPE = "IVF_FLAT"
_NLIST = 1024

# 打个比方 ivf索引就像是把一所小学的小学生分班管理，nlist就是班级数量，假设我们按年龄大小分成nlist个班级，你查询时的nprobe是要查找的班级
# 你要找的人大约有12岁，所以就从高年级里选出nprobe个班，然后你又加了个查询条件“我要找名字叫李明的小朋友”
# 如果那nprobe个班级里没有叫“李明”的小盆友，那就查不到了
# 如果你把nprobe设成nlist的值，相当于全校搜索，那就能查出来了，他可能在一年级的某个班里


def memory_record_to_milvus_dict(
    owner: CollectionSchemaOwner, record: MemoryRecord
) -> dict[str, Any]:
    ret_dict = {}

    concrete_record = {}

    if owner.casefold() == CollectionSchemaOwner.Qna.name.casefold():
        concrete_record = record.to_qna_memory_record()
    elif owner.casefold() == CollectionSchemaOwner.Search.name.casefold():
        concrete_record = record.to_search_memory_record()
    else:
        raise ValueError("Unsupported schema owner.")

    for key, value in vars(concrete_record).items():
        if value is not None:
            ret_dict[key] = value
    return ret_dict


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

        collection.create_index(EMBEDDING_FIELD, index_params=index_param)

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
        records: list[MemoryRecord]
    ) -> list[str]:
        if collection_name not in utility.list_collections():
            raise SystemError(
                f"Collection {collection_name} does not exist, cannot upsert."
            )
        for r in records:
            print(r)
        data_list = [memory_record_to_milvus_dict(owner, record) for record in records]

        collection = Collection(collection_name)
        ids = collection.upsert(data=data_list).primary_keys
        collection.flush()

        return ids

    def _get_schema_by_owner(
        self, owner: CollectionSchemaOwner, dimension: int
    ) -> CollectionSchema:
        if owner.casefold() == CollectionSchemaOwner.Qna.name.casefold():
            return CollectionSchema(
                create_qna_field_schema(dimensions=dimension), enable_dynamic_field=True
            )
        elif owner.casefold() == CollectionSchemaOwner.Search.name.casefold():
            return CollectionSchema(
                create_search_field_schema(dimensions=dimension),
                enable_dynamic_field=True,
            )
        elif owner.casefold() == CollectionSchemaOwner.Faq.name.casefold():
            return CollectionSchema(
                create_faq_field_schema(dimensions=dimension), enable_dynamic_field=True
            )
        else:
            raise ValueError("Unsupported schema owner.")

    def _get_milvus_dict(
        self, owner: CollectionSchemaOwner, memory_records: list[MemoryRecord]
    ) -> Dict[str, Any]:
        if owner.casefold() == CollectionSchemaOwner.Qna.name.casefold():
            qna_memory_records = self._get_qna_memory_records(owner, memory_records)
            return {record.id: record for record in qna_memory_records}
        elif owner.casefold() == CollectionSchemaOwner.Search.name.casefold():
            search_memory_records = self._get_search_memory_records(
                owner, memory_records
            )
            return {record.id: record for record in search_memory_records}
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