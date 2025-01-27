
import re


def remove_html_comments(html_content):
    # 正则表达式模式，用于匹配 HTML 注释
    pattern = r"<!--.*?-->"
    # 使用 re.sub() 函数替换匹配的注释为空白字符串
    cleaned_content = re.sub(pattern, "", html_content, flags=re.DOTALL)
    return cleaned_content


# 示例 HTML 内容
html_content = """  
<!-- PdfToMarkdownPatterns.PageSection.FooterBegin -->
<!-- 12/2012 @ 2010 McDonald's Corp. 生产

 -->
<!-- PdfToMarkdownPatterns.PageSection.FooterEnd -->
<!-- PdfToMarkdownPatterns.CommentPlaceHolder -->
<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第7页 -->
<!-- PdfToMarkdownPatterns.CommentPlaceHolder -->
<!-- PdfToMarkdownPatterns.PageSection.HeaderBegin -->
<!-- 生产生产

 -->
<!-- PdfToMarkdownPatterns.PageSection.HeaderEnd --> 
"""

# 移除 HTML 注释
cleaned_html = remove_html_comments(html_content)
print(cleaned_html.strip())