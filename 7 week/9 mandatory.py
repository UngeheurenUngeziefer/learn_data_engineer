# Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

f = open('input.txt', 'r', encoding='utf8')
myDict = dict()

for string in f:
    for letter in string.split():
        if myDict.get(letter, 0) == 0:
            myDict[letter] = 1
        else:
            x = myDict[letter] + 1
            myDict[letter] = x
            x = 0

print(max(sorted(myDict.keys()), key=lambda x: myDict[x]))

f.close()
