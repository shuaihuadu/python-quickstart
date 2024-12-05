language = "zh"

model_file_path = f"BM25_CORPUS_{language.upper()}_MODEL_FILE_PATH"

print(f"BM25 Embedding language:{language}, use model file:{model_file_path}")


chunks = "your_chunks_value"
rows = "your_rows_value"
message = "更新了{0}向量库Chunks {1}行".format(chunks, rows)
print(message)