
import pandas as pd

# 假设 query_result 是一个包含字典的列表
query_result = [
    {
        "id": 1,
        "collection_id": 10,
        "page_number": 2,
        "book_id": 1,
        "book_name": "Book A",
        "source_url": "url1",
        "chunk_index": 2,
        "chunk_content": "Content A",
    },
    {
        "id": 2,
        "collection_id": 10,
        "page_number": 1,
        "book_id": 1,
        "book_name": "Book A",
        "source_url": "url2",
        "chunk_index": 1,
        "chunk_content": "Content B",
    },
    {
        "id": 3,
        "collection_id": 20,
        "page_number": 3,
        "book_id": 2,
        "book_name": "Book B",
        "source_url": "url3",
        "chunk_index": 2,
        "chunk_content": "Content C",
    },
    {
        "id": 4,
        "collection_id": 10,
        "page_number": 4,
        "book_id": 1,
        "book_name": "Book A",
        "source_url": "url4",
        "chunk_index": 2,
        "chunk_content": "Content D",
    },
    # 更多记录...
]

# 将查询结果转换为 DataFrame
df = pd.DataFrame(query_result)

# 先对 DataFrame 按照 page_number 和 chunk_index 进行排序
df_sorted = df.sort_values(by=["page_number", "chunk_index"])

# 根据指定字段去重，保留每组的第一条记录
df_unique = df_sorted.drop_duplicates(
    subset=["book_id", "chunk_index", "collection_id"], keep="first"
)

# 将去重后的结果转换回列表形式（如果需要）
unique_query_result = df_unique.to_dict(orient="records")

print(unique_query_result)