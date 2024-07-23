# Python虚拟环境

`python.exe -m venv MilvusNoteBook\.venv`

1. 创建Python虚拟环境，python -m venv dev_env
2. 激活环境：dev_env/Scripts/activate
3. 安装虚拟环境的pip包（根据需要）


# 使用requirements.txt

1. 可以使用pip freeze > requirements.txt创建，也可以手动创建
2. 编辑requirements.txt，添加需要的包及版本。例如：
``` python
pymilvus==2.4.4
milvus-model==0.2.3
```
也可以不写版本，默认最新版：
```python
pymilvus
milvus-model
```
使用以下命令安装：
`pip install -r requirements.txt`

# 在虚拟环境中使用requirements.txt
