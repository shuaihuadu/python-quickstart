import json
from typing import Dict, List
from milvus_model.sparse.bm25.bm25 import BM25EmbeddingFunction
from milvus_model.sparse.bm25.tokenizers import build_default_analyzer
import numpy as np
from scipy.sparse import csr_array, csr_matrix

analyzer = build_default_analyzer(language="zh")

data_path = r"D:\hu2-prep\MilvusNoteBook\data\data-0001.json"

model_path = r"D:\hu2-prep\MilvusNoteBook\models\corpus_cn_completed.json"

# with open(data_path, "r", encoding="utf-8") as file:
#     data = json.load(file)
# print(data)


@staticmethod
def sparse_to_dict(sparse_array: csr_array) -> Dict[int, float]:
    row_indices, col_indices = sparse_array.nonzero()
    non_zero_values = sparse_array.data
    result_dict = {}
    for col_index, value in zip(col_indices, non_zero_values):
        result_dict[col_index] = value
    return result_dict


docs = [
    "今天（12日），国务院发布关于修改《全国年节及纪念日放假办法》的决定，自2025年1月1日开始施行，同时发布关于2025年部分节假日安排的通知。",
    # "全体公民放假的假日增加2天，即农历除夕和5月2日，放假总天数由11天增加至13天。",
    # "明确调休规则。此次将调休规则进行明确和公布，群众可以对照规则自行规划安排未来假期，更好保障休息休假。",
]

bm25_ef = BM25EmbeddingFunction(analyzer)

bm25_ef.load(model_path)

docs_embeddings = bm25_ef.encode_documents(docs)

print(docs_embeddings)

data = [sparse_to_dict(sparse_array) for sparse_array in docs_embeddings]
print(data)

dense_array = docs_embeddings.toarray()
result_list = dense_array.flatten().tolist()
print(result_list)