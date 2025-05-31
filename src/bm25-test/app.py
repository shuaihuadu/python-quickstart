# import jieba
import jieba
from bm25 import generate_query_bm25

jieba.load_userdict(r"./files/jieba/hu_dict.txt")
tokenizer = jieba.Tokenizer()
tokenizer.initialize()

jieba.get_FREQ = lambda k, d=None: tokenizer.FREQ.get(k, d)
jieba.add_word = tokenizer.add_word
jieba.calc = tokenizer.calc
jieba.cut = tokenizer.cut
jieba.lcut = lambda sentence: tokenizer.lcut(sentence, cut_all=True)
jieba.cut_for_search = tokenizer.cut_for_search
jieba.lcut_for_search = tokenizer.lcut_for_search
jieba.del_word = tokenizer.del_word
jieba.get_DAG = tokenizer.get_DAG
jieba.get_dict_file = tokenizer.get_dict_file
jieba.initialize = tokenizer.initialize
jieba.load_userdict = tokenizer.load_userdict
jieba.set_dictionary = tokenizer.set_dictionary
jieba.suggest_freq = tokenizer.suggest_freq
jieba.tokenize = tokenizer.tokenize
jieba.user_word_tag_tab = tokenizer.user_word_tag_tab

jieba.tokenizer = tokenizer


# with open(r"./files/jieba/hu_dict.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#     for word in lines:
#         jieba.add_word(word=word)

# query_bm25 = generate_query_bm25("zh", "麦")
# print(query_bm25)
# query_bm25 = generate_query_bm25("zh", "牛肉饼")
# print(query_bm25)
# query_bm25 = generate_query_bm25("zh", "猪柳蛋")
# print(query_bm25)
# query_bm25 = generate_query_bm25("zh", "薯条")
# print(query_bm25)

query = "麦香鸡"

print(jieba.lcut(query))

query_bm25 = generate_query_bm25("zh", query=query)
print(query_bm25)
