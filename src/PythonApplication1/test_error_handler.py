
from flask import Flask, jsonify
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)


# 定义一个全局的错误处理器
@app.errorhandler(Exception)
def handle_unhandled_exception(e):
    # 记录异常信息（可选）
    app.logger.error(f"Unhandled Exception: {e}")
    # 返回一个通用的500错误响应
    response = {
        "message": "An internal server error occurred.",
        "error": str(e),  # 在生产环境中，通常不返回详细的错误信息
    }
    return jsonify(response), 500


# 示例资源
@api.route("/example")
class ExampleResource(Resource):
    def get(self):
        # 这里故意引发一个异常来测试错误处理
        raise Exception("This is an unhandled exception.")
        return {"message": "Hello, World!"}


if __name__ == "__main__":
    # 将端口更改为8080
    app.run(debug=True, port=8080)