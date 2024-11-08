from ast import List
from flask import request
from flask_restx import Namespace, Resource, fields
from milvus import milvus_service
from milvus.apis.api_constants import RESPONSE_MODEL
from milvus.milvus_service import MilvusService
from milvus.models.memory_record import MemoryRecord

milvus_service = MilvusService()

ns = Namespace("entity", description="Milvus Collection的Entity的操作")

memory_record_model = ns.model(
    "MemoryRecord",
    {
        "id": fields.String(required=True, description="数据的Id"),
        "text": fields.String(required=True, description="文本内容"),
        "embedding": fields.List(fields.Float, required=True, description="文本向量"),
        "meta": fields.String(required=True, description="元数据的JSON字符串内容"),
    },
)

response_model = ns.model("Response", RESPONSE_MODEL)


@ns.route("/<string:owner>/collection/<string:collection_name>/upsert")
class Upsert(Resource):
    @ns.expect([memory_record_model])
    @ns.marshal_with(response_model, code=201)
    def post(self, owner, collection_name):
        """新增/修改Milvus Collection的数据"""
        data = request.json
        if isinstance(data, list):
            memory_records: List[MemoryRecord] = [
                MemoryRecord(
                    id=item["id"],
                    text=item["text"],
                    embedding=item.get("embedding", []),
                    meta=item["meta"],
                )
                for item in data
            ]
            milvus_service.upsert_batch(
                owner=owner, collection_name=collection_name, records=memory_records
            )
        else:
            raise Exception("Data must be an array")