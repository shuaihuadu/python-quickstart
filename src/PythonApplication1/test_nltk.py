import nltk

nltk.data.path.append("./nltk_data")

stopwords = nltk.corpus.stopwords.words('english')
print(stopwords[:10])