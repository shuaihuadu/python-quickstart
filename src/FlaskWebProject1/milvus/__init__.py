from flask import Flask
from milvus.apis import milvus_api

app = Flask(__name__)
milvus_api.init_app(app=app)
