import glob
import json
import os
from typing import Dict, List
from milvus_model.sparse.bm25.bm25 import BM25EmbeddingFunction
from milvus_model.sparse.bm25.tokenizers import build_default_analyzer
from scipy.sparse import csr_array

from book_chunk import BookChunk, ChunkData

# 现有的Model的路径
model_path = r"D:\hu2-prep\MilvusNoteBook\models\corpus_cn_completed.json"

data_folder_path = r"D:\hu2-prep\MilvusNoteBook\data"
file_pattern = os.path.join(data_folder_path, "data-*.json")
data_files = glob.glob(file_pattern)

# 读取数据
data_files = [r"D:\hu2-prep\MilvusNoteBook\data\data-0001.json"]

data = []

for data_file in data_files:
    with open(data_file, "r", encoding="utf-8") as file:
        data += json.load(file)

print(f"加载的数据数量：{len(data)}")

book_chunks = []

for item in data:
    id = item.get("id")
    book_id = item.get("bookId")
    book_name = item.get("bookName")
    chunk_content = item.get("chunkContent")
    book_chunk = BookChunk(id, book_id, book_name, chunk_content)
    book_chunks.append(book_chunk)


@staticmethod
def sparse_to_dict(sparse_array: csr_array) -> Dict[int, float]:
    row_indices, col_indices = sparse_array.nonzero()
    non_zero_values = sparse_array.data
    result_dict = {}
    for col_index, value in zip(col_indices, non_zero_values):
        result_dict[col_index] = value
    return result_dict


analyzer = build_default_analyzer(language="zh")
chunk_datas: list[ChunkData] = []

for item in book_chunks:
    docs = [item.chunk_content]

    bm25_ef = BM25EmbeddingFunction(analyzer)

    # 使用现有的Model
    bm25_ef.load(model_path)

    docs_embeddings = bm25_ef.encode_documents(docs)
    # Compressed Sparse Row sparse array of dtype 'float32'
    # print(docs_embeddings)

    # data = [sparse_to_dict(sparse_array) for sparse_array in docs_embeddings]
    # print(data)

    dense_array = docs_embeddings.toarray()
    result_list = dense_array.flatten().tolist()

    # print(result_list)

    chunk_data = ChunkData(
        id=item.id,
        book_id=item.book_id,
        book_name=item.book_name,
        chunk_content=item.chunk_content,
        bm25_data=result_list,
    )
    chunk_datas.append(chunk_data)

# print(f"转换后的数据数量：{len(chunk_datas)}")

# print(chunk_datas)

# 获取当前工作目录
current_directory = os.getcwd()
# 构建 data 目录的路径
data_directory = os.path.join(current_directory, "data")

# 构建文件的完整路径
data_file_save_path = os.path.join(data_directory, "bm25_data_result.json")

# 将 JSON 数据写入文件
with open(data_file_save_path, "w", encoding="utf-8") as json_file:
    # json.dump(chunk_datas, json_file, ensure_ascii=False, indent=4)
    json.dump(
        [chunk.to_dict() for chunk in chunk_datas],
        json_file,
        ensure_ascii=False,
        indent=4,
    )

try:
    if os.name == "nt":  # Windows
        os.startfile(data_directory)
    elif os.name == "posix":  # macOS or Linux
        subprocess.run(["open", data_directory])  # macOS
        # subprocess.run(['xdg-open', data_directory])  # Linux
except Exception as e:
    print(f"无法打开文件夹: {e}")