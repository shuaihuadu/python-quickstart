from pymilvus import DataType, FieldSchema
from milvus.constants import ID_FIELD,EMBEDDING_FIELD,VARCHAR_MAX_LENGTH

COLLECTION_ID_FIELD = "collectionId"
PAGE_NUMBER_FIELD = "pageNumber"
SEARCHABLE_FIELD = "searchable"
BOOK_ID_FIELD = "bookId"
BOOK_NAME_FIELD = "bookName"
VERSION_ID_FIELD = "versionId"
VERSION_STATUS_FIELD = "versionStatus"
MATERIAL_ID_FIELD = "materialId"
CATEGORY_FIELD = "category"
SOURCE_TYPE_FIELD = "sourceType"
SOURCE_ID_FIELD = "sourceId"
SOURCE_URL_FIELD = "sourceUrl"
CHUNK_INDEX_FIELD = "chunkIndex"
CHUNK_TYPE_FIELD = "chunkType"
CHUNK_CONTENT_FIELD = "chunkContent"
PAGE_COUNT_FIELD = "pageCount"
WORD_COUNT_FIELD = "wordCount"
QUERYABLE_FIELD = "queryable"
CHUNK_ATOM_TYPE_FIELD = "chunkAtomType"
LEVEL_FIELD = "level"
TOKEN_COUNT_FIELD = "tokenCount"
TIMESTAMP_FIELD = "timestamp"

def create_field_schemas(dimensions: int) -> list[FieldSchema]:
    """创建QnA的Milvus Collection使用的字段的Schema"""
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
        FieldSchema(name=QUERYABLE_FIELD, dtype=DataType.BOOL),
        FieldSchema(
            name=CHUNK_ATOM_TYPE_FIELD,
            dtype=DataType.VARCHAR,
            max_length=VARCHAR_MAX_LENGTH,
        ),
        FieldSchema(name=LEVEL_FIELD, dtype=DataType.INT32),
        FieldSchema(name=TOKEN_COUNT_FIELD, dtype=DataType.INT32),
        FieldSchema(
            name=TIMESTAMP_FIELD, dtype=DataType.VARCHAR, max_length=VARCHAR_MAX_LENGTH
        ),
    ]
