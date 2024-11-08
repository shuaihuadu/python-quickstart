import os
from dotenv import load_dotenv
from milvus import app

load_dotenv(override=True)

# print("SERVER_HOST:", os.environ.get("SERVER_HOST"))
# print("SERVER_PORT:", os.environ.get("SERVER_PORT"))

if __name__ == "__main__":
    HOST = os.environ.get("SERVER_HOST", "localhost")

    try:
        PORT = int(os.environ.get("SERVER_PORT", "5555"))
    except ValueError:
        PORT = 5555

    app.run(HOST, PORT)
