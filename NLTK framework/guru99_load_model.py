from gensim.models import Word2Vec

model = Word2Vec.load('model.bin')
vocab = list(model.wv.key_to_index)

similar_words = model.wv.most_similar('thanks', topn=100)	

dissimlar_words = model.wv.doesnt_match('See you later, thanks for visiting' \
                                                                    .split())

words_dict = {'hi': 'hello',
              'please': 'see',
              'pay': 'cash',
              'hi': 'back'}

for key, value in words_dict.items():
    similarity = model.wv.similarity(key, value)
    print(f'Similarity between {key} and {value} is : {similarity}')

similar = model.wv.similar_by_word('pay')
print(similar)
