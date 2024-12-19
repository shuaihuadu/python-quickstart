from pymilvus import utility, connections

connections.connect("default", host="localhost", port=19530)

collections = utility.list_collections()

print(collections)