from flask import Flask
from flask_restful import Api
from milvus.milvus_apis import initialize_api


def create_app():
    app = Flask(__name__)
    api = Api(app)
    initialize_api(api)
    return app