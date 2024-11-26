import os
import json
from dataclasses import dataclass


@dataclass
class ChunkResponse:
    start_part: int
    end_part: int
    file_path: str

    def __init__(self, start_part: int, end_part: int, file_path: str):
        self.start_part = start_part
        self.end_part = end_part
        self.file_path = file_path


@dataclass
class ChunkDataItem:
    page: int
    part: int
    text: str

    def __init__(self, page: int, part: int, text: str):
        self.page = page
        self.part = part
        self.text = text


@dataclass
class BM25ChunkData:
    name: str
    items: list[ChunkDataItem]

    def __init__(self, name: str, items: list[ChunkDataItem]):
        self.name = name
        self.items = items


def extract_name(filename):
    base_file_name = os.path.splitext(os.path.basename(filename))[0]
    # 找到最后两个下划线的位置
    parts = base_file_name.rsplit("_", 2)
    # 返回前面的部分作为 {name}
    return "_".join(parts[:-2])


def parse_json_file(file_path: str) -> BM25ChunkData:

    with open(file_path, "r", encoding="utf-8") as file:
        name = extract_name(file.name)
        data = json.load(file)

        items = [
            ChunkDataItem(item["page"], item["part"], item["text"]) for item in data
        ]

        result = BM25ChunkData(name=name, items=items)
    return result


def process_directory(chunks_directory: str) -> list[BM25ChunkData]:
    result = []
    for entry in os.listdir(chunks_directory):
        file_path = os.path.join(chunks_directory, entry)
        if os.path.isfile(file_path):
            data = parse_json_file(file_path)
            result.append(data)
    return result


result: list[BM25ChunkData] = process_directory(
    r"D:\McDonalds\HU2\compose\python-src\resources\bin\chunks"
)
print(len(result))