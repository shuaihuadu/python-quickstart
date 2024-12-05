from datetime import datetime


class SearchMemoryRecord:
    def __init__(
        self,
        collection_id: str,
        book_id: str,
        version_id: str,
        version_tag: str,
        chunk_content: str,
        chunk_type: str,
        page_number: int,
        chunk_index: int,
    ):
        self.id = f"{collection_id}-{book_id}-{version_id}-{page_number}-{chunk_index}"
        self.collection_id = collection_id
        self.page_number = page_number
        self.searchable = False
        self.book_ancestors = ""
        self.book_id = book_id
        self.book_name = ""
        self.version_id = version_id
        self.version_status = ""
        self.version_tag = version_tag
        self.material_id = ""
        self.category = ""
        self.source_type = ""
        self.source_id = ""
        self.source_url = ""
        self.chunk_index = chunk_index
        self.chunk_type = chunk_type
        self.chunk_content = chunk_content
        self.chunk_source = ""
        self.page_count = 0
        self.word_count = len(chunk_content)
        self.timestamp = datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "collection_id": self.collection_id,
            "page_number": self.page_number,
            "searchable": self.searchable,
            "book_ancestors": self.book_ancestors,
            "book_id": self.book_id,
            "book_name": self.book_name,
            "version_id": self.version_id,
            "version_status": self.version_status,
            "version_tag": self.version_tag,
            "material_id": self.material_id,
            "category": self.category,
            "source_type": self.source_type,
            "source_id": self.source_id,
            "source_url": self.source_url,
            "chunk_index": self.chunk_index,
            "chunk_type": self.chunk_type,
            "chunk_content": self.chunk_content,
            "chunk_source": self.chunk_source,
            "page_count": self.page_count,
            "word_count": self.word_count,
            "timestamp": self.timestamp,
        }


record = SearchMemoryRecord(
    collection_id="default",
    book_id="book-1865",
    version_id="version-001",
    version_tag="培训 炸制",
    chunk_content="汉堡和薯条",
    chunk_type="Search",
    page_number=10,
    chunk_index=343,
)

# print(record.id)
# print(len(record.id))
print(record.to_dict())

{
    "id": "default-book-1865-version-001-10-343",
    "collection_id": "default",
    "page_number": 10,
    "searchable": True,
    "book_ancestors": "{}",
    "book_id": "book-1865",
    "book_name": "XXX手册",
    "version_id": "version-001",
    "version_status": "Active",
    "version_tag": "培训 炸制",
    "material_id": "",
    "category": "201",
    "source_type": "",
    "source_id": "",
    "source_url": "http://",
    "chunk_index": 343,
    "chunk_type": "Search",
    "chunk_content": "汉堡和薯条",
    "chunk_source": "BookChunk",
    "page_count": 0,
    "word_count": 5,
    "timestamp": "2024-12-03T19:10:29.304857",
}