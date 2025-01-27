
import os
import json


def merge_json_files(directory, output_file):
    # 初始化一个空列表来存储所有的 JSON 数据
    merged_data = []

    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        # 构建文件的完整路径
        file_path = os.path.join(directory, filename)

        # 检查文件是否是 JSON 文件
        if filename.endswith(".json"):
            with open(file_path, "r", encoding="utf-8") as file:
                # 读取 JSON 文件内容
                data = json.load(file)
                # 将数据添加到合并列表中
                merged_data.extend(data)

    # 将合并后的数据写入输出文件
    with open(output_file, "w", encoding="utf-8") as output:
        json.dump(merged_data, output, ensure_ascii=False, indent=4)


# 使用该函数
directory_path = r"D:\McDonalds\HU2\compose\python-src\local_test_data\Book-4515\search_bm25_embeddings_new\en"  # 替换为你的目录路径
output_file_path = r"D:\McDonalds\HU2\compose\python-src\local_test_data\Book-4515\merged_output_en2.json"  # 替换为你想要的输出文件名
merge_json_files(directory_path, output_file_path)