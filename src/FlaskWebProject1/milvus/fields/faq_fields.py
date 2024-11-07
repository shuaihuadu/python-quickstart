from pymilvus import DataType, FieldSchema
from milvus.constants import ID_FIELD, EMBEDDING_FIELD, VARCHAR_MAX_LENGTH

QUESTION_FIELD = "question"
ANSWER_FIELD = "answer"
COLLECTION_FIELD = "collectionId"
SEARCHABLE_FIELD = "searchable"
BOOK_ID_FIELD = "bookId"
BOOK_NAME_FIELD = "bookName"
VERSION_ID_FIELD = "versionId"
VERSION_STATUS_FIELD = "versionStatus"
MATERIAL_ID_FIELD = "materialId"
CATEGORY_FIELD = "category"
SOURCE_TYPE_FIELD = "sourceType"
SOURCE_URL_FIELD = "sourceUrl"
PAGE_NUMBER_FIELD = "pageNumber"
TIMESTAMP_FIELD = "timestamp"
IS_VERIFIED_FIELD = "isVerified"


def create_field_schemas(dimensions: int) -> list[FieldSchema]:
    """创建FAQ的Milvus Collection使用的字段的Schema"""
    return [
        FieldSchema(
            name=ID_FIELD,
            dtype=DataType.VARCHAR,
            is_primary=True,
            auto_id=False,
            max_length=100,
        ),
        FieldSchema(
            name=EMBEDDING_FIELD,
            dtype=DataType.FLOAT_VECTOR,
            dim=dimensions,
        ),
        FieldSchema(
            name=QUESTION_FIELD, dtype=DataType.VARCHAR, max_length=VARCHAR_MAX_LENGTH
        ),
        FieldSchema(
            name=ANSWER_FIELD, dtype=DataType.VARCHAR, max_length=VARCHAR_MAX_LENGTH
        ),
        FieldSchema(
            name=COLLECTION_FIELD, dtype=DataType.VARCHAR, max_length=VARCHAR_MAX_LENGTH
        ),
        FieldSchema(name=SEARCHABLE_FIELD, dtype=DataType.BOOL),
        FieldSchema(
            name=BOOK_ID_FIELD, dtype=DataType.VARCHAR, max_length=VARCHAR_MAX_LENGTH
        ),
        FieldSchema(
            name=BOOK_NAME_FIELD, dtype=DataType.VARCHAR, max_length=VARCHAR_MAX_LENGTH
        ),
        FieldSchema(
            name=VERSION_ID_FIELD, dtype=DataType.VARCHAR, max_length=VARCHAR_MAX_LENGTH
        ),
        FieldSchema(
            name=VERSION_STATUS_FIELD,
            dtype=DataType.VARCHAR,
            max_length=VARCHAR_MAX_LENGTH,
        ),
        FieldSchema(
            name=MATERIAL_ID_FIELD,
            dtype=DataType.VARCHAR,
            max_length=VARCHAR_MAX_LENGTH,
        ),
        FieldSchema(
            name=CATEGORY_FIELD, dtype=DataType.VARCHAR, max_length=VARCHAR_MAX_LENGTH
        ),
        FieldSchema(
            name=SOURCE_TYPE_FIELD,
            dtype=DataType.VARCHAR,
            max_length=VARCHAR_MAX_LENGTH,
        ),
        FieldSchema(
            name=SOURCE_URL_FIELD, dtype=DataType.VARCHAR, max_length=VARCHAR_MAX_LENGTH
        ),
        FieldSchema(name=PAGE_NUMBER_FIELD, dtype=DataType.INT32),
        FieldSchema(
            name=TIMESTAMP_FIELD, dtype=DataType.VARCHAR, max_length=VARCHAR_MAX_LENGTH
        ),
        FieldSchema(name=IS_VERIFIED_FIELD, dtype=DataType.BOOL),
    ]