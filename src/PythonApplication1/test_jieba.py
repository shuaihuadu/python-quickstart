import jieba

# 待分词的文本
text = "我爱北京天安门"

# 精确模式分词
seg_list = jieba.cut(text, cut_all=False)
print("精确模式: " + "/ ".join(seg_list))

# 全模式分词
seg_list = jieba.cut(text, cut_all=True)
print("全模式: " + "/ ".join(seg_list))

# 搜索引擎模式分词
seg_list = jieba.cut_for_search(text)
print("搜索引擎模式: " + "/ ".join(seg_list))