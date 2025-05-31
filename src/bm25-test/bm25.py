import os
from re import A
from milvus_model.sparse.bm25.tokenizers import build_default_analyzer, StopwordFilter
from milvus_model.sparse.bm25.bm25 import BM25EmbeddingFunction


def generate_query_bm25(language: str, query: str):

    bm25_ef: BM25EmbeddingFunction = get_bm25_ef(language=language)

    data = generate_bm25_query_embedding(bm25_ef=bm25_ef, text=query)

    return {int(k): float(v) for k, v in data.items()}


def generate_document_bm25(language: str, document: str):

    bm25_ef: BM25EmbeddingFunction = get_bm25_ef(language=language)

    data = generate_bm25_embedding(bm25_ef=bm25_ef, text=document)

    return {int(k): float(v) for k, v in data.items()}


def generate_bm25_embedding(
    bm25_ef: BM25EmbeddingFunction, text: str
) -> dict[int, float]:

    docs = [text]
    docs_embedding = bm25_ef.encode_documents(docs)

    # 将CSR矩阵转换为字典

    bm25_data = {
        index: value
        for index, value in zip(docs_embedding.indices, docs_embedding.data)
    }

    return bm25_data


def generate_bm25_query_embedding(
    bm25_ef: BM25EmbeddingFunction, text: str
) -> dict[int, float]:

    print("bm25_ef相关的参数：")
    print(f"bm25_ef.avgdl:{bm25_ef.avgdl}")
    print(f"bm25_ef.b:{bm25_ef.b}")
    print(f"bm25_ef.corpus_size:{bm25_ef.corpus_size}")
    print(f"bm25_ef.epsilon:{bm25_ef.epsilon}")
    print(f"len(bm25_ef.idf):{len(bm25_ef.idf)}")
    print(f"bm25_ef.num_workers:{bm25_ef.num_workers}")
    print(f"bm25_ef.analyzer.name:{bm25_ef.analyzer.name}")
    print(f"len(bm25_ef.analyzer.filters):{len(bm25_ef.analyzer.filters)}")
    print(f"bm25_ef.analyzer:{bm25_ef.analyzer}")
    print("bm25_ef相关的参数结束")

    # 获取对象的所有属性和方法
    # attributes = dir(bm25_ef)
    # excluded_attributes = {"idf"}

    # for attribute in attributes:
    #     if not attribute.startswith("__") and attribute not in excluded_attributes:
    #         value = getattr(bm25_ef, attribute)
    #         print(f"{attribute}: {value}")

    docs = [text]
    embedding = bm25_ef.encode_queries(docs)

    # 将CSR矩阵转换为字典

    bm25_data = {
        index: value for index, value in zip(embedding.indices, embedding.data)
    }

    return bm25_data


def get_bm25_ef(language: str, load_model_file: bool = True):

    # stopwords_to_remove = _get_stopwords_to_remove()

    analyzer = build_default_analyzer(language=language)

    # for f in analyzer.filters:
    #     if isinstance(f, StopwordFilter):
    #         f.stopwords.difference_update(stopwords_to_remove)

    bm25_ef = BM25EmbeddingFunction(analyzer=analyzer, num_workers=1)

    if load_model_file:
        model_file = r"./files/corpus_zh_completed.json"

        bm25_ef.load(model_file)

    return bm25_ef


def _get_stopwords_to_remove() -> set[str]:

    stopwords_to_remove = set()

    file_path = r"./files/stopwords_to_remove.txt"

    with open(file_path, "r", encoding="utf-8") as file:
        data = [line.strip() for line in file if line.strip()]
        stopwords_to_remove = set(data)

    return stopwords_to_remove
