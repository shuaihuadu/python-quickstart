class BookChunk:
    def __init__(self, id: str, book_id: str, book_name: str, chunk_content: str):
        self.id = id
        self.book_id = book_id
        self.book_name = book_name
        self.chunk_content = chunk_content

    def __repr__(self):
        return f"BookChunk(id={self.id},book_id={self.book_id},book_name={self.book_name},chunk_content={self.chunk_content})"

    def to_dict(self):
        return {
            "id": self.id,
            "book_id": self.book_id,
            "book_name": self.book_name,
            "chunk_content": self.chunk_content,
        }

class ChunkData(BookChunk):

    def __init__(
        self,
        id: str,
        book_id: str,
        book_name: str,
        chunk_content: str,
        bm25_data: list[float],
    ):
        # 调用父类的构造函数来初始化继承的属性
        super().__init__(id, book_id, book_name, chunk_content)
        self.bm25_data = bm25_data

    def to_dict(self):
        # 使用父类的 to_dict 方法并添加 bm25_data
        data = super().to_dict()
        data["bm25_data"] = self.bm25_data
        return data

    def __repr__(self):
        return f"ChunkData(id={self.id}, book_id={self.book_id}, book_name={self.book_name}, chunk_content={self.chunk_content}, bm25_data={self.bm25_data})"