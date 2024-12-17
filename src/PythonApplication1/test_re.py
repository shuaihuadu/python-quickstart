
import re

text = """
流程模块-流程查询流程查询
操作路径一:门户>左侧功能菜单区>查询流程
操作路径–:门户>功能模块区>流程>左侧功能菜单区>查询流程
<!-- PdfToMarkdownPatterns.PageSection.FooterBegin -->
<!-- 搜索  
-->
爱上对方就会看见浩方fsdkjhkdsf
<!-- PdfToMarkdownPatterns.PageSection.FooterEnd -->"""

# 使用正则表达式匹配并清除目标文本
cleaned_text = re.sub(
    r"<!-- PdfToMarkdownPatterns\.PageSection\.FooterBegin -->.*?<!-- PdfToMarkdownPatterns\.PageSection\.FooterEnd -->",
    "",
    text,
    flags=re.DOTALL,
)

print(cleaned_text)

text = """金拱门DMS系统 用户使用手册2021.10  
<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第1页 -->
目录
M
小
M
1 登录后门户
2 流程模块
3 档案管理模块
M
4 流程说明  
<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第2页 -->
01 登录后门户  
<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第3页 -->
注册后门户介绍，覅速度很快函数的返回  
<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第1页 -->
登录后门户介绍，反动势力回顾客服电话公开反对  
<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第2页 -->
登录后门户功能介绍
一、主要模块:
门户、流程、档案管理
二、个人门户
流程中心【待办事宜、已办事宜、办结事宜、追踪事宜】
档案管理制度、信息中心、快捷搜索栏、退出系统、档案归档、档案打包、档案归属变更、档案仓储变更、档案借阅、档案遗失、待办中心、我的请求、查询流程、已办事宜。

<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第1页 -->"""

# 使用正则表达式分割文本
pages = re.split(
    r"<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第\d+页 -->",
    text,
)


# V1: 去除每个页面的前后空白字符
pages = [page.strip() for page in pages if page.strip()]

# 输出结果
for i, page in enumerate(pages, start=1):
    print(f"第{i}页内容：{page}")


# V2: 去除每个页面的前后空白字符，并移除空白行
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




金拱门DMS系统 用户使用手册
2021.10

<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第1页 -->

目录
M
小
M
1 登录后门户
2 流程模块
3 档案管理模块
M
4 流程说明

<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第2页 -->

01 登录后门户

<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第3页 -->

注册后门户介绍，覅速度很快函数的返回

<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第1页 -->

登录后门户介绍，反动势力回顾客服电话公开反对

<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第2页 -->

登录后门户功能介绍
一、主要模块:
门户、流程、档案管理
二、个人门户
流程中心【待办事宜、已办事宜、办结事宜、追踪事宜】
档案管理制度、信息中心、快捷搜索栏、退出系统、档案归档、档案打包、档案归属变更、档案仓储变更、档案借阅、档案遗失、待办中心、我的请求、查询流程、已办事宜。

<!-- 这是使用FormRecognizer进行的Pdf转换后的Markdown中的分页符，当前是第1页 -->

期望输出结果：
第1页内容：
金拱门DMS系统 用户使用手册
2021.10
注册后门户介绍，覅速度很快函数的返回

第2页内容：
目录
M
小
M
1 登录后门户
2 流程模块
3 档案管理模块
M
4 流程说明
登录后门户介绍，反动势力回顾客服电话公开反对
第3页内容：
01 登录后门户