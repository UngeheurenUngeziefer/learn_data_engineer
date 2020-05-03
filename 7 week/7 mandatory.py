x = open('input.txt')
a = x.read()

counter = {}
for word in a.split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')
