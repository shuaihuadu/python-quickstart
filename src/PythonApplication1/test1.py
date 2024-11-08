
import json


class QnaMemoryRecord:
    def __init__(self):
        self.collection_id = ""
        self.page_number = 0
        self.searchable = False
        self.book_id = ""
        self.book_name = ""
        self.version_id = ""
        self.version_status = ""
        self.material_id = ""
        self.category = ""
        self.source_type = ""
        self.source_id = ""
        self.source_url = ""
        self.chunk_index = 0
        self.chunk_content = ""
        self.chunk_type = ""
        self.page_count = 0
        self.word_count = 0
        self.queryable = False
        self.chunk_atom_type = ""
        self.level = 0
        self.token_count = 0
        self.timestamp = ""
        self.id = ""

    def __str__(self) -> str:
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)
        record = cls()
        for key, value in data.items():
            if hasattr(record, key):
                setattr(record, key, value)
        return record

    def generate_id(self) -> str:
        if self.chunk_index < 1:
            return f"{self.book_id}_{self.version_id}_{self.chunk_type}"
        else:
            return f"{self.book_id}_{self.version_id}_{self.chunk_type}_{str(self.page_number).zfill(3)}_{str(self.chunk_index).zfill(6)}"


# 创建几个 QnaMemoryRecord 对象并设置所有属性
record1 = QnaMemoryRecord()
record1.collection_id = "col1"
record1.page_number = 1
record1.searchable = True
record1.book_id = "book1"
record1.book_name = "Book One"
record1.version_id = "v1"
record1.version_status = "published"
record1.material_id = "mat1"
record1.category = "fiction"
record1.source_type = "pdf"
record1.source_id = "src1"
record1.source_url = "http://example.com/book1"
record1.chunk_index = 1
record1.chunk_content = "This is the content of chunk 1."
record1.chunk_type = "introduction"
record1.page_count = 100
record1.word_count = 500
record1.queryable = True
record1.chunk_atom_type = "paragraph"
record1.level = 1
record1.token_count = 50
record1.timestamp = "2023-10-01T12:00:00Z"

record2 = QnaMemoryRecord()
record2.collection_id = "col2"
record2.page_number = 2
record2.searchable = False
record2.book_id = "book2"
record2.book_name = "Book Two"
record2.version_id = "v2"
record2.version_status = "draft"
record2.material_id = "mat2"
record2.category = "non-fiction"
record2.source_type = "epub"
record2.source_id = "src2"
record2.source_url = "http://example.com/book2"
record2.chunk_index = 2
record2.chunk_content = "This is the content of chunk 2."
record2.chunk_type = "chapter"
record2.page_count = 200
record2.word_count = 1000
record2.queryable = False
record2.chunk_atom_type = "section"
record2.level = 2
record2.token_count = 100
record2.timestamp = "2023-10-02T12:00:00Z"

record3 = QnaMemoryRecord()
record3.collection_id = "col3"
record3.page_number = 3
record3.searchable = True
record3.book_id = "book3"
record3.book_name = "Book Three"
record3.version_id = "v3"
record3.version_status = "archived"
record3.material_id = "mat3"
record3.category = "science"
record3.source_type = "html"
record3.source_id = "src3"
record3.source_url = "http://example.com/book3"
record3.chunk_index = 3
record3.chunk_content = "This is the content of chunk 3."
record3.chunk_type = "appendix"
record3.page_count = 300
record3.word_count = 1500
record3.queryable = True
record3.chunk_atom_type = "list"
record3.level = 3
record3.token_count = 150
record3.timestamp = "2023-10-03T12:00:00Z"

record1.id = record1.generate_id()
record2.id = record2.generate_id()
record3.id = record3.generate_id()

# 将对象转换为 JSON 字符串
json_str1 = str(record1)
json_str2 = str(record2)
json_str3 = str(record3)


data = {"id": record1.id, "text": record1.chunk_content, "meta": json_str1}


print(data)
data_json_str = json.dumps(data, indent=2)
print(data_json_str)