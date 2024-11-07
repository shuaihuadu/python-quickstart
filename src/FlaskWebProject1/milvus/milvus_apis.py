from flask_restful import Api
from milvus.milvus_resources import CreateCollection


def initialize_api(api: Api):
    api.add_resource(CreateCollection, "/api/milvus/collection/<string:owner>/create")
