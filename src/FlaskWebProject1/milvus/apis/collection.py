from flask import request
from flask_restx import Namespace, Resource, fields
from milvus.apis.api_constants import RESPONSE_MODEL
from milvus.milvus_service import MilvusService
from milvus.models.response import Response


milvus_service = MilvusService()

ns = Namespace("collection", description="Milvus Collection的操作")

create_model = ns.model(
    "CollectionCreateRequest",
    {
        "collection_name": fields.String(required=True, description="Collection名称"),
        "metric_type": fields.String(required=True, description="向量计算度量类型"),
        "dimension": fields.Integer(required=True, description="向量维度"),
    },
)

response_model = ns.model("Response", RESPONSE_MODEL)


@ns.route("/create/<string:owner>")
class Create(Resource):
    @ns.expect(create_model)
    @ns.marshal_with(response_model, code=201)
    def post(self, owner):
        """创建新的Collection"""
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

        return Response(message=f"{owner} collection created successfully"), 201


@ns.route("/list")
class List(Resource):
    @ns.marshal_with(response_model, code=200)
    def get(self):
        """列出所有的Collection"""
        collections = milvus_service.get_collections()
        return Response(data=collections), 200


@ns.route("/delete/<string:collection_name>")
class Delete(Resource):
    def post(self, collection_name):
        milvus_service.delete_collection(collection_name=collection_name, all=True)
        return (
            Response(message=f"Collection {collection_name} deleted successfully"),
            200,
        )