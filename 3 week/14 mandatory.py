s = input()

indexFirst = 0
n = len(s)
for i in range(n):
    if s[i] == ' ':
        indexFirst += 1
print(indexFirst+1)
