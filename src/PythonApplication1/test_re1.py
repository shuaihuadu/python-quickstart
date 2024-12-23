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
pages = re.split(regex_pattern, text)

pages = [page.strip() for page in pages if page.strip()]

print(pages)

paged_chunks = []

for i, page in enumerate(pages, start=1):
    print(f"第{i}页内容：{page}")

cleaned_pages = []
for page in pages:
    # 去除前后空白字符
    page = page.strip()
    # 移除空白行
    lines = page.splitlines()
    non_empty_lines = [line for line in lines if line.strip()]
    cleaned_page = "\n".join(non_empty_lines)
    if cleaned_page:
        cleaned_pages.append(cleaned_page)

# 输出结果
for i, page in enumerate(cleaned_pages, start=1):
    print(f"第{i}页内容：{page}")
