s = input()

indexFirst = None
indexLast = None
# indexes = []
n = len(s)
for i in range(n):
    if s[i] == 'h' or s[i] == 'H':
        indexFirst = i
        break
for j in range(n-1, 0, -1):
    if s[j] == 'h' or s[j] == 'H':
        indexLast = j
        break
if indexFirst:
    s1 = s[:indexFirst] + s[indexLast+1:]
    print(s1)
else:
    pass
