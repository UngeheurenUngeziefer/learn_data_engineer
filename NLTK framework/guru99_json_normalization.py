import json
import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from textblob import Word
import string

# open json
json_file = r'Data_Engineer\NLTK framework\sample.json' 
with open(json_file,'r') as f:
    data = json.load(f)

# json to df, merge all parts
df = pd.DataFrame(data)
df['patterns'] = df['patterns'].apply(', '.join)

stop = stopwords.words('english')
df['patterns'] = df['patterns'].apply(lambda x: ' ' \
                .join(x.lower() for x in x.split()))
print('\nAll words in lowercase ---------------------------------------------')
print(df['patterns'])

df['patterns'] = df['patterns'].apply(lambda x: ' ' \
                .join(x for x in x.split() if x not in string.punctuation))
print('\nRemove punctuation -------------------------------------------------')
print(df['patterns'])

df['patterns'] = df['patterns'].str.replace('[^\w\s]', '', regex=True)
print('\nRemove all non-word and non-space with -----------------------------')
print(df['patterns'])

df['patterns'] = df['patterns'].apply(lambda x: ' ' \
                .join(x for x in x.split() if  not x.isdigit()))
print('\nRemove all digits --------------------------------------------------')
print(df['patterns'])

df['patterns'] = df['patterns'].apply(lambda x: ' ' \
                .join(x for x in x.split() if not x in stop))
print('\nFrequent english stopwords removed ---------------------------------')
print(df['patterns'])

df['patterns'] = df['patterns'].apply(lambda x: ' ' \
                .join([Word(word).lemmatize() for word in x.split()]))
print('\nLemmatize ----------------------------------------------------------')
print(df['patterns'])
