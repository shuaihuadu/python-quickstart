from flask_restx import fields


API_PREFIX = "/api/milvus"

RESPONSE_MODEL = {
    "code": fields.String(description="系统操作结果代码"),
    "message": fields.String(description="响应相关的消息"),
    "data": fields.Wildcard(
        fields.Raw, description="响应相关的数据内容"
    ),
}