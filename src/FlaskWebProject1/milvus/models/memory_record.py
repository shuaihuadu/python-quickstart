import json
from typing import Optional
from numpy import ndarray
from milvus.models.qna_memory_record import QnaMemoryRecord
from milvus.models.search_memory_record import SearchMemoryRecord


class MemoryRecord:
    def __init__(self, id: str, text: str, embedding: ndarray, meta: str):
        self.id = id
        self.text = text
        self.embedding = embedding
        self.meta = meta

    @staticmethod
    def is_valid_json(s: str) -> bool:
        try:
            json.loads(s)
            return True
        except json.JSONDecodeError:
            return False

    def to_search_memory_record(self) -> Optional["SearchMemoryRecord"]:
        if self.is_valid_json(self.meta):
            return SearchMemoryRecord.from_json(self.meta)
        return None

    def to_qna_memory_record(self) -> Optional["QnaMemoryRecord"]:
        if self.is_valid_json(self.meta):
            return QnaMemoryRecord.from_json(self.id, self.embedding, self.meta)
        return None