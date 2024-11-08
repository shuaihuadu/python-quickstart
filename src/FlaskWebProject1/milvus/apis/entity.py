from ast import List
from flask import request
from flask_restx import Namespace, Resource, fields
from milvus import milvus_service
from milvus.apis.api_constants import RESPONSE_MODEL
from milvus.milvus_service import MilvusService
from milvus.models.memory_record import MemoryRecord
from milvus.models.response import Response
from numpy import array
from json import dumps

milvus_service = MilvusService()

ns = Namespace("entity", description="Milvus Collection的Entity的操作")

memory_record_model = ns.model(
    "MemoryRecord",
    {
        "id": fields.String(required=True, description="数据的id"),
        "text": fields.String(required=True, description="文本内容"),
        "embedding": fields.List(fields.Float, required=True, description="文本向量"),
        "meta": fields.String(required=True, description="元数据的JSON字符串内容"),
    },
)

search_request_model = ns.model(
    "SearchRequest",
    {
        "embedding": fields.List(fields.Float, required=True, description="搜索的向量"),
        "limit": fields.Integer(required=True, description="返回的结果数"),
        "min_relevance_score": fields.Integer(
            required=True, description="相关性分数阈值"
        ),
        "with_embeddings": fields.Boolean(
            required=False, description="搜索结果是否包含embedding，默认是False"
        ),
        "ids": fields.List(
            fields.String, required=False, description="需要过滤的数据的id"
        ),
        "book_ids": fields.List(
            fields.String, required=False, description="需要过滤的数据的book_id"
        ),
        "categories": fields.List(
            fields.String, required=False, description="需要过滤的数据的category"
        ),
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

            ids = milvus_service.upsert_batch(
                owner=owner, collection_name=collection_name, records=memory_records
            )

            return (
                Response(
                    code=200,
                    message=f"Entities of collection {collection_name} upsert successfully",
                    data=ids,
                ),
                201,
            )
        else:
            raise Exception("Data must be an array")


@ns.route("/collection/<string:collection_name>/delete")
class Delete(Resource):
    @ns.expect([str])
    @ns.marshal_with(response_model, code=201)
    def delete(self, collection_name):
        data = request.json
        if isinstance(data, list[str]):
            milvus_service.delete_batch(collection_name, data)

            return (
                Response(
                    message=f"Entities of {collection_name} delete successfully",
                ),
                200,
            )


@ns.route("/<string:owner>/collection/<string:collection_name>/search")
class Search(Resource):
    @ns.expect(search_request_model)
    @ns.marshal_with(response_model, 200)
    def post(self, owner, collection_name):
        """搜索与embedding最相近的limit条的记录"""
        data = request.json
        embedding = (data.get("embedding", []),)
        if embedding is not None:
            embedding = array(embedding)

        result = milvus_service.search(
            owner=owner,
            collection_name=collection_name,
            embedding=embedding,
            limit=data["limit"],
            min_relevance_score=data["min_relevance_score"],
            with_embeddings=data["with_embeddings"],
            ids=data.get("ids", []),
            book_ids=data.get("book_ids", []),
            categories=data.get("categories", []),
        )

        return Response(data=result), 200