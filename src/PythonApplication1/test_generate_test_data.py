import random
import json


def generate_test_data():
    test_data1 = {
        "page": 1,
        "part": 1,
        "embedding": [random.uniform(-1.0, 1.0) for _ in range(3072)],
    }
    test_data2 = {
        "page": 2,
        "part": 1,
        "embedding": [random.uniform(-1.0, 1.0) for _ in range(3072)],
    }
    return [test_data1, test_data2]


def save_to_json(data, filename):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)


# 生成测试数据
test_datas = generate_test_data()

# 将数据保存到 JSON 文件
save_to_json(test_datas, "test_data.json")

print("数据已保存到 test_data.json 文件中。")