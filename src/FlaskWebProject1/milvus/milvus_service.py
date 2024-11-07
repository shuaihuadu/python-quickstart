from pymilvus import Collection, CollectionSchema, utility, connections
from typing import Optional
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

# 索引参数
_INDEX_TYPE = "IVF_FLAT"
_NLIST = 1024

# 打个比方 ivf索引就像是把一所小学的小学生分班管理，nlist就是班级数量，假设我们按年龄大小分成nlist个班级，你查询时的nprobe是要查找的班级
# 你要找的人大约有12岁，所以就从高年级里选出nprobe个班，然后你又加了个查询条件“我要找名字叫李明的小朋友”
# 如果那nprobe个班级里没有叫“李明”的小盆友，那就查不到了
# 如果你把nprobe设成nlist的值，相当于全校搜索，那就能查出来了，他可能在一年级的某个班里


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

        self.collections: dict[str, Collection] = {}

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
        schema = []
        if owner.casefold() == CollectionSchemaOwner.Qna.name.casefold():
            schema = CollectionSchema(create_qna_field_schema(dimensions=dimension))
        elif owner.casefold() == CollectionSchemaOwner.Search.name.casefold():
            schema = CollectionSchema(create_search_field_schema(dimensions=dimension))
        elif owner.casefold() == CollectionSchemaOwner.Faq.name.casefold():
            schema = CollectionSchema(create_faq_field_schema(dimensions=dimension))
        else:
            raise ValueError("Unsupported schema owner.")

        index_param = {
            "index_type": _INDEX_TYPE,
            "params": {"nlist": _NLIST},
            "metric_type": metric_type,
        }

        if utility.has_collection(collection_name=collection_name) and overwrite:
            utility.drop_collection(collection_name=collection_name)

        self.collections[collection_name] = Collection(
            name=collection_name, schema=schema, consistency_level=consistency
        )

        self.collections[collection_name].create_index(
            EMBEDDING_FIELD, index_params=index_param
        )