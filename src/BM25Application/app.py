# 假设你已经有一个 JSON 数组
import json


json_array = [
    {
        "id": "1",
        "book_id": "101",
        "book_name": "Example Book 1",
        "chunk_content": "This is a chunk of the first book.",
        "bm25_data": [0.5, 0.8, 0.3],
    },
    {
        "id": "2",
        "book_id": "102",
        "book_name": "Example Book 2",
        "chunk_content": "This is a chunk of the second book.",
        "bm25_data": [0.6, 0.7, 0.4],
    },
]

# 将 JSON 数组写入到 JSON 文件
with open("chunk_data.json", "w", encoding="utf-8") as json_file:
    json.dump(json_array, json_file, ensure_ascii=False, indent=4)

print("JSON 数据已成功写入到 chunk_data.json 文件中。")