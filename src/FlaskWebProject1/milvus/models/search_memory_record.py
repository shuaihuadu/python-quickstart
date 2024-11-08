import json

from numpy import ndarray


class SearchMemoryRecord:
    def __init__(self, id: str, embedding: ndarray):
        self.collection_id = ""
        self.page_number = 0
        self.searchable = False
        self.book_ancestors = ""
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
        self.timestamp = ""
        self.id = (id,)
        self.embedding = embedding

    def __str__(self) -> str:
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, id: str, embedding: ndarray, json_str: str):
        data = json.loads(json_str)
        record = cls(id, embedding)
        for key, value in data.items():
            if hasattr(record, key):
                setattr(record, key, value)