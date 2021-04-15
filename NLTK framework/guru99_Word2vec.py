from sklearn.feature_extraction.text import CountVectorizer

import nltk
import gensim
from nltk.corpus import abc


# words frequency
data_corpus = ["guru99 is the best sitefor online tutorials. \
                I love to visit guru99."]

vectorizer = CountVectorizer()
vocabulary = vectorizer.fit(data_corpus)
X = vectorizer.transform(data_corpus)
X = X.toarray()
vocabulary = vocabulary.get_feature_names()
