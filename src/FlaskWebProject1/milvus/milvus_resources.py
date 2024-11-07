from flask import request
from flask_restful import Resource
from milvus.constants import CollectionSchemaOwner
from milvus.milvus_service import MilvusService

milvus_service = MilvusService()


class CreateCollection(Resource):
    def post(self, owner):
        data = request.json
        collection_name = data["collection_name"]
        metric_type = data["metric_type"]
        dimension = data["dimension"]
        milvus_service.create_collection(
            owner=owner,
            collection_name=collection_name,
            dimension=dimension,
            metric_type=metric_type,
        )

        return {"code": 200, "message": f"{owner} collection created successfully"}
