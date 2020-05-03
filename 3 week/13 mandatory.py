s = input()

indexFirst = None
n = len(s)
for i in range(n):
    if s[i] == ' ':
        indexFirst = i
        break
if indexFirst:
    print(s[indexFirst + 1::] + ' ' + s[0:indexFirst])
else:
    pass
