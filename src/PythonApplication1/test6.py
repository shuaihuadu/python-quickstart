import uuid  
from dataclasses import dataclass, field  
from numpy import ndarray  
from datetime import datetime  
  
@dataclass  
class SearchMemoryRecord:  
    book_id: str  
    version_id: str  
    version_tag: str  
    chunk_content: str  
    chunk_type: str  
    page_number: int  
    chunk_index: int  
    embedding: ndarray  
    bm25_embedding: ndarray  
    collection_id: str = ""  
    searchable: bool = False  
    book_ancestors: str = ""  
    book_name: str = ""  
    version_status: str = ""  
    material_id: str = ""  
    category: str = ""  
    source_type: str = ""  
    source_id: str = ""  
    source_url: str = ""  
    page_count: int = 0  
    word_count: int = 0  
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())  
    id: str = field(default_factory=lambda: str(uuid.uuid4()))  
  
# 示例对象  
record = SearchMemoryRecord(  
    book_id="123",  
    version_id="v1",  
    version_tag="tag1",  
    chunk_content="content",  
    chunk_type="type",  
    page_number=1,  
    chunk_index=0,  
    embedding=ndarray([]),  # 这里需要提供实际的 ndarray  
    bm25_embedding=ndarray([])  # 这里需要提供实际的 ndarray  
)  
  
print(record)  

# 使用 asdict 将 dataclass 对象转换为字典  
from dataclasses import asdict  
record_dict = asdict(record)  
  
# 打印结果  
print(record_dict)  