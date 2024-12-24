
import re

text = "在2023年，科技的进步让我们的生活发生了巨大的变化。The development of AI has been remarkable, and it continues to evolve rapidly. 例如，智能手机的功能越来越强大，它们不仅可以用来打电话，还可以用来进行视频会议、拍摄高质量的照片等等。与此同时，5G网络的普及也让数据传输速度提升了10倍以上！这使得我们可以在任何地方都保持连接，无论是在家还是在办公室。总之，科技的进步让我们的生活更加便捷和高效。"

# 使用正则表达式提取非中文字符
non_chinese_content = re.findall(r"[^\u4e00-\u9fff]+", text)

# 将提取的内容合并成一个字符串
result = "".join(non_chinese_content)

# print(result)

# 使用正则表达式提取非中文的字母和数字
non_chinese_content = re.findall(r"[A-Za-z0-9]+", text)

# 将提取的内容合并成一个字符串
result = " ".join(non_chinese_content)

print(result)