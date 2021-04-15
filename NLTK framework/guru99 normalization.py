from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from collections import defaultdict

# test sentences
words= ["wait", "waiting", "waited", "waits"]
sentence="Hello Guru99, You have to build a very good site \
          and I love visiting your site."
sentence2 = "studies studying cries cry"
words = word_tokenize(sentence)

# stemming list of words
def stemming_words(words):
    ps = PorterStemmer()
    for word in words:
        rootWord = ps.stem(word)
        print(rootWord)

# stemming some text
def stemming_text(text):
    porter_stemmer = PorterStemmer()
    tokenization = nltk.word_tokenize(text)
    for word in tokenization:
        print(f"Stemming for {word} is {porter_stemmer.stem(word)}")

# lemmatization
def lemmatization(text):
	wordnet_lemmatizer = WordNetLemmatizer()
	tokenization = nltk.word_tokenize(text)
	for word in tokenization:
		print(f"Lemma for {word} is {wordnet_lemmatizer.lemmatize(word)}")

# wordnet
tag_map = defaultdict(lambda: wn.NOUN)
tag_map['J'] = wn.ADJ
tag_map['V'] = wn.VERB
tag_map['R'] = wn.ADV

text = "guru99 is a totally new kind of learning experience."
tokens = word_tokenize(text)
lemma_function = WordNetLemmatizer()
for token, tag in pos_tag(tokens):
    lemma = lemma_function.lemmatize(token, tag_map[tag[0]])
    print(token, "=>", lemma)
