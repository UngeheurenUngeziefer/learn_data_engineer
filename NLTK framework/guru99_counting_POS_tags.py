from collections import Counter
import nltk

text = " Guru99 is one of the best sites to learn WEB, \
        SAP, Ethical Hacking and much more online."
text2 = "Guru99 is the site where you can find the best \
         tutorials for Software Testing     Tutorial, SAP Course \
         for Beginners. Java Tutorial for Beginners and much more. \
         Please     visit the site guru99.com and much more."

# tags counter
lower_case = text.lower()
tokens = nltk.word_tokenize(lower_case)
tags = nltk.pos_tag(tokens)
counts = Counter(tag for word, tag in tags)

# frequency distribution
words = nltk.tokenize.word_tokenize(text2)
fd = nltk.FreqDist(words)
fd.plot()
