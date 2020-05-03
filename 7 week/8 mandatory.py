n = int(input())
dict = {}
dict2 = {}
for i in range(n):
    word1, word2 = input().split()
    dict[word1] = word2
    dict2[word2] = word1
word3 = input()
if word3 in dict:
    print(dict[word3])
else:
    print(dict2[word3])
