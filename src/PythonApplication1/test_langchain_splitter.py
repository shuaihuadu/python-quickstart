from langchain.text_splitter import RecursiveCharacterTextSplitter

separator = "【这是手动添加的用来拆分文本块的自定义分隔符】"

separators = [separator] + ["\n\n", "\n", " "]

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1, 
    chunk_overlap=0, 
    separators=separators, 
    keep_separator=False
)

# 注意事项
# 1.分隔符和chunk_size有关，如果使用自定义分隔符则需要设置一个合理的chunk_size，保证按照自定义的分隔符进行切片
# 2.如果使用自定义分隔符，则需要禁用掉之前切片器默认的分隔符
# 处理逻辑
# 1.识别需要切片的文本中是否包含自定义分隔符
# 2.如果包含，则构建自定义的切片器，设定chunk_size=合理的chunk_size、separators=[自定义分隔符]、keep_separator=False

# 示例文本
text = f"这是一个示例文本。我们将使用自定义分隔符来分割这个文本。在这个示例中，custom_separators列表定义了四种分隔符：双换行符、单换行符、空格和空字符串。{separator}RecursiveCharacterTextSplitter将按照这个顺序尝试分割文本，直到满足chunk_size和chunk_overlap的要求。"

# 使用 text_splitter 分割文本
chunks = splitter.split_text(text)

# 输出分割后的文本块
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}")