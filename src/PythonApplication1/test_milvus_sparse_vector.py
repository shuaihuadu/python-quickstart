from pymilvus import MilvusClient, DataType

collection_name = "my_sparse_collection"

client = MilvusClient(url="http://localhost:19530")

client.drop_collection(collection_name)

schema = client.create_schema(auto_id=True, enable_dynamic_fields=True)

schema.add_field(
    field_name="pk", datatype=DataType.VARCHAR, is_primary=True, max_length=100
)

schema.add_field(field_name="sparse_vector1", datatype=DataType.SPARSE_FLOAT_VECTOR)

index_params = client.prepare_index_params()

index_params.add_index(
    "sparse_vector1",
    index_name="sparse_inverted_index",
    index_type="SPARSE_INVERTED_INDEX",
    metric_type="IP",
    params={"drop_ratio_build": 0.2},
)

client.create_collection(
    collection_name=collection_name, schema=schema, index_params=index_params
)

sparse_vectors = [
    {"sparse_vector1": {1: 0.5, 100: 0.3, 500: 0.8}},
    {"sparse_vector1": {10: 0.1, 200: 0.7, 1000: 0.9}},
]

client.insert(collection_name=collection_name, data=sparse_vectors)

# search_params = {"params": {"drop_ratio_search": 0.2}}

# query_vector = [{1: 0.2, 50: 0.4, 1000: 0.7}]

# res = client.search(
#     collection_name="my_sparse_collection",
#     data=query_vector,
#     limit=3,
#     output_fields=["pk"],
#     search_params=search_params,
# )

# print(res)
