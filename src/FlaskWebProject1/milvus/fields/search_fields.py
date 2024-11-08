from pymilvus import DataType, FieldSchema
from milvus.constants import (
    ID_FIELD,
    EMBEDDING_FIELD,
    DYNAMIC_FIELD,
    VARCHAR_MAX_LENGTH,
)

COLLECTION_ID_FIELD = "collection_id"
PAGE_NUMBER_FIELD = "page_number"
SEARCHABLE_FIELD = "searchable"
BOOK_ANCESTORS_FIELD = "book_ancestors"
BOOK_ID_FIELD = "book_id"
BOOK_NAME_FIELD = "book_name"
VERSION_ID_FIELD = "version_id"
VERSION_STATUS_FIELD = "version_status"
MATERIAL_ID_FIELD = "material_id"
CATEGORY_FIELD = "category"
SOURCE_TYPE_FIELD = "source_type"
SOURCE_ID_FIELD = "source_id"
SOURCE_URL_FIELD = "source_url"
CHUNK_INDEX_FIELD = "chunk_index"
CHUNK_TYPE_FIELD = "chunk_type"
CHUNK_CONTENT_FIELD = "chunk_content"
PAGE_COUNT_FIELD = "page_count"
WORD_COUNT_FIELD = "word_count"
TIMESTAMP_FIELD = "timestamp"

OUTPUT_FIELDS_WITH_EMBEDDING = [
    ID_FIELD,
    EMBEDDING_FIELD,
    CHUNK_CONTENT_FIELD,
    DYNAMIC_FIELD,
]

OUTPUT_FIELDS_WITH_OUT_EMBEDDING = [
    ID_FIELD,
    CHUNK_CONTENT_FIELD,
    DYNAMIC_FIELD,
]


def create_field_schemas(dimensions: int) -> list[FieldSchema]:
    """创建Search的Milvus Collection使用的字段的Schema"""
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
            name=COLLECTION_ID_FIELD,
            dtype=DataType.VARCHAR,
            max_length=VARCHAR_MAX_LENGTH,
        ),
        FieldSchema(name=PAGE_NUMBER_FIELD, dtype=DataType.INT32),
        FieldSchema(name=SEARCHABLE_FIELD, dtype=DataType.BOOL),
        FieldSchema(name=BOOK_ANCESTORS_FIELD, dtype=DataType.JSON),
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
            name=SOURCE_ID_FIELD, dtype=DataType.VARCHAR, max_length=VARCHAR_MAX_LENGTH
        ),
        FieldSchema(
            name=SOURCE_URL_FIELD, dtype=DataType.VARCHAR, max_length=VARCHAR_MAX_LENGTH
        ),
        FieldSchema(name=CHUNK_INDEX_FIELD, dtype=DataType.INT32),
        FieldSchema(
            name=CHUNK_TYPE_FIELD, dtype=DataType.VARCHAR, max_length=VARCHAR_MAX_LENGTH
        ),
        FieldSchema(
            name=CHUNK_CONTENT_FIELD,
            dtype=DataType.VARCHAR,
            max_length=VARCHAR_MAX_LENGTH,
        ),
        FieldSchema(name=PAGE_COUNT_FIELD, dtype=DataType.INT32),
        FieldSchema(name=WORD_COUNT_FIELD, dtype=DataType.INT32),
        FieldSchema(
            name=TIMESTAMP_FIELD, dtype=DataType.VARCHAR, max_length=VARCHAR_MAX_LENGTH
        ),
    ]