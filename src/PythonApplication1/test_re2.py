import re


class PagedChunkContent:
    def __init__(self, page_number: int = 0, chunk_content: str = ""):
        self.page_number = page_number
        self.chunk_content = chunk_content


text = """第一页的内容
<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第1页 -->
第二页的内容

<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第2页 -->

第三页的内容

<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第3页 -->
第一秒的内容
<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第1秒 -->
第二页的第二部分的内容
<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第2页 -->
第一页的第三部分内容

<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第1页 -->"""

regex_pattern = r"<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第(\d+)(页|秒) -->"

# 使用正则表达式分割文本
split_result = re.split(regex_pattern, text)

# 使用字典来存储每个页码的内容
page_content_dict = {}

for i in range(0, len(split_result) - 1, 3):
    chunk_content = split_result[i].strip()
    page_number = int(split_result[i + 1])

    if page_number not in page_content_dict:
        page_content_dict[page_number] = []

    page_content_dict[page_number].append(chunk_content)

# 创建 PagedChunkContent 对象列表
paged_chunks = []
for page_number, contents in page_content_dict.items():
    combined_content = "\n".join(contents)
    paged_chunks.append(PagedChunkContent(page_number, combined_content))

# 打印结果
for chunk in paged_chunks:
    print(f"Page Number: {chunk.page_number}, Content:\n{chunk.chunk_content}\n")