class MemoryRecordHelper:

    @staticmethod
    def generate_entity_id(
        chunk_index: int,
        book_id: str,
        version_id: str,
        chunk_type: str,
        page_number: int,
    ) -> str:
        if chunk_index < 1:
            return f"{book_id}_{version_id}_{chunk_type}"
        else:
            return f"{book_id}_{version_id}_{chunk_type}_{str(page_number).zfill(3)}_{str(chunk_index).zfill(6)}"