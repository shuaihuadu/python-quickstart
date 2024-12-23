
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

text = """第一页的内容
<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第1页 -->
第二页的内容

<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第2页 -->

第三页的内容"""

text1 = """第一页的内容"""
regex_pattern = r"<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第(\d+)(页|秒) -->"


# 使用正则表达式分割文本
split_result = re.split(regex_pattern, text)

# 存储每个页码和其内容
page_content_dict = {}

# 处理正常的分割结果
for i in range(0, len(split_result) - 1, 3):
    chunk_content = split_result[i].strip()
    page_number = int(split_result[i + 1])
    if page_number not in page_content_dict:
        page_content_dict[page_number] = []
    page_content_dict[page_number].append(chunk_content)

# 如果存在不在正则表达式解析结果内容中的块，则使用0作为其页码
if len(split_result) % 3 == 1:
    last_chunk_content = split_result[-1].strip()
    if last_chunk_content:
        # 使用 0 来标记没有页码的内容
        if 0 not in page_content_dict:
            page_content_dict[0] = []
        page_content_dict[0].append(last_chunk_content)

# 语音的解析结果中，相同秒数的内容需要合并到一起(理论上来说pdf解析的结果中的页面分隔符都是唯一的，不会出现相同的页面分隔符)
paged_chunks = []

for page_number, contents in page_content_dict.items():
    combined_content = "\n".join(contents)
    paged_chunks.append(PagedChunkContent(page_number, combined_content))

# 打印结果
for chunk in paged_chunks:
    print(f"Page Number: {chunk.page_number}, Content:\n{chunk.chunk_content}\n")
    print("==========================================")
