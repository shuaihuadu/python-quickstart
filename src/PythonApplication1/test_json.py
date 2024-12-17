
import json
import os

# 定义文件路径
file_path = "meta.json"

# 定义新的数据
new_data = {"data_unit": "Page", "data_length": 100}

# 检查文件是否存在
if not os.path.exists(file_path):
    # 如果文件不存在，创建一个新文件并写入新的数据
    with open(file_path, "w") as file:
        json.dump(new_data, file, indent=2)
else:
    # 如果文件存在，读取现有数据
    with open(file_path, "r") as file:
        existing_data = json.load(file)

    # 更新现有数据中的指定字段
    existing_data["data_unit"] = new_data["data_unit"]
    existing_data["data_length"] = new_data["data_length"]

    # 将更新后的数据写回文件
    with open(file_path, "w") as file:
        json.dump(existing_data, file, indent=2)

print(f"Meta file processed: {file_path}")