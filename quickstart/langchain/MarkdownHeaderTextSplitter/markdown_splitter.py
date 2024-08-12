from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_markdown(fileName):
    with open(fileName, "r", encoding="utf-8") as file:
        markdown_document = file.read()

    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
        ("####", "Header 4"),
        ("#####", "Header 5"),
        ("######", "Header 6"),
    ]

    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on,
        strip_headers=True,  # 是否把Header的内容剥离出去
    )

    return markdown_splitter.split_text(markdown_document)


def split_content(markdown_splits):
    # 在每个Markdown切片的结果，可以使用普通的文本切片器
    chunk_size = 200
    chunk_overlap = 0
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )

    return text_splitter.split_documents(markdown_splits)
