
import json
import numpy as np


class BM25EmbeddingItem:
    def __init__(self, page: int, part: int, embedding: list[dict[int, float]]):
        self.page = page
        self.part = part
        self.embedding = embedding

    def to_dict(self):
        # 将 numpy.int32 转换为 int
        converted_embedding = [
            {int(k): v for k, v in emb.items()} for emb in self.embedding
        ]
        return {"page": self.page, "part": self.part, "embedding": converted_embedding}

    @staticmethod
    def from_dict(data: dict):
        return BM25EmbeddingItem(
            page=data["page"], part=data["part"], embedding=data["embedding"]
        )


# 序列化列表并保存到文件
def serialize_list_to_file(items: list[BM25EmbeddingItem], filename: str):
    with open(filename, "w") as file:
        # 将对象列表转换为字典列表
        dict_list = [item.to_dict() for item in items]
        json.dump(dict_list, file, indent=4)


# 从文件中反序列化列表
def deserialize_list_from_file(filename: str) -> list[BM25EmbeddingItem]:
    with open(filename, "r") as file:
        dict_list = json.load(file)
        return [BM25EmbeddingItem.from_dict(data) for data in dict_list]


# 示例用法
items = [
    BM25EmbeddingItem(page=1, part=2, embedding=[{np.int32(1): 0.5, np.int32(2): 0.3}]),
    BM25EmbeddingItem(page=2, part=3, embedding=[{np.int32(3): 0.7, np.int32(4): 0.2}]),
]

# 序列化并保存到文件
serialize_list_to_file(items, "bm25_items.json")

# 从文件中反序列化
loaded_items = deserialize_list_from_file("bm25_items.json")
for item in loaded_items:
    print("Deserialized:", item.page, item.part, item.embedding)