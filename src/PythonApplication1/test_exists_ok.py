import os

# 当 exists_ok 设置为 False（默认值）时，如果目标目录已经存在，os.makedirs 会引发一个 FileExistsError 异常
# os.makedirs(r"C:\Users\shuai\Desktop\temp-0030", exist_ok=False)

# 当 exists_ok 设置为 True 时，如果目标目录已经存在，os.makedirs 不会引发异常，而是静默地继续执行；如果目录不存在，os.makedirs 会自动创建所需的目录结构
os.makedirs(r"C:\Users\shuai\Desktop\temp-0030", exist_ok=True)