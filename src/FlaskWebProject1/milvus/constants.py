from enum import Enum

ID_FIELD = "id"
EMBEDDING_FIELD = "embedding"
DYNAMIC_FIELD = "$meta"
OPENAI_EMBEDDING_VECTOR_SIZE = 1536
VARCHAR_MAX_LENGTH = 65535
DEFAULT_METRIC_TYPE = "CONSINE"


class CollectionSchemaOwner(Enum):
    Search = (1,)
    Qna = (2,)
    Faq = (3,)
    Simlarity = 4