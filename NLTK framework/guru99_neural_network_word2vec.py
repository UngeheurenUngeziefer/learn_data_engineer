from gensim.models import Word2Vec
from guru99_json_normalization import df

import string
from gensim.models import Word2Vec
import logging
from nltk.corpus import stopwords
from textblob import Word
import json
import pandas as pd

bigger_list = []

for i in df['patterns']:
    li = list(i.split(' '))
    bigger_list.append(li)

model = Word2Vec(bigger_list, min_count=1, vector_size=300, workers=4)
model.save('word2vec.model')
model.save('model.bin')
