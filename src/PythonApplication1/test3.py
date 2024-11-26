import os

def extract_name(filename):
    base_file_name = os.path.splitext(os.path.basename(filename))[0]
    # 找到最后两个下划线的位置
    parts = base_file_name.rsplit("_", 2)
    # 返回前面的部分作为 {name}
    return "_".join(parts[:-2])


print(extract_name("complex_name_part_0001_0002.json"))
print(extract_name("【大苏打】1_0001_0002.json"))
print(extract_name("按时发的_0001_0002.json"))