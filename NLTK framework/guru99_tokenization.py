from nltk.tokenize import RegexpTokenizer

# separate words without punctuation
tokenizer = RegexpTokenizer(r'\w+')
string = 'Hello Guru99, You have build a very good site and I love \
          visiting your site.'
filterdText = tokenizer.tokenize(string)


# separate words and punctuation
from nltk.tokenize import word_tokenize
text = "God is Great! I won a lottery."
filteredText = word_tokenize(text)


# separate sentences
from nltk.tokenize import sent_tokenize
text = "God is Great! I won a lottery."
filteredText = sent_tokenize(text)


# pos tagging
from nltk import pos_tag
from nltk import RegexpParser
# separate words
text ="learn php from guru99 and make study easy".split()
# tokenize (dividing into tags)
tokens_tag = pos_tag(text)
# regex
patterns= """mychunk:{<NN.?>*<VBD.?>*<JJ.?>*<CC>?}"""
chunker = RegexpParser(patterns)
# chunking
output = chunker.parse(tokens_tag)


import nltk
text = "learn php from guru99"
# dividing into tokens (separate words)
tokens = nltk.word_tokenize(text)
print(tokens)
# pos tags, separate words with tags (pats of speech)
tag = nltk.pos_tag(tokens)
print(tag)
# regex
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(tag)
print(result)
# draw tree of tags
result.draw()
