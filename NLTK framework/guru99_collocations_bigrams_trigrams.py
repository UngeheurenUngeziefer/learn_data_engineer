import nltk

# bigrams and trigrams used for next word prediction 
# and counting of frequency of pair usage
text = "Guru99 is a totally new kind of learning experience."
tokens = nltk.word_tokenize(text)
bigrams_list = list(nltk.bigrams(tokens))
trigrams_list = list(nltk.trigrams(tokens))
print(bigrams_list)
print(trigrams_list)

