from flask import Blueprint
from flask_restx import Api, fields
from .collection import ns as collection_namespace
from .api_constants import API_PREFIX

milvus_api = Api(
    version="1.0",
    title="Milvus 操作的REST API",
    description="包括对指定的Milvus数据库中的Collections和Entities的操作",
    prefix=API_PREFIX,
    doc="/",
)

milvus_api.add_namespace(collection_namespace)