s = list(map(int, input().split()))
a, b, c, d = s[0], s[1], s[2], s[3]
set1 = set(range(min(a, b), max(a, b) + 1))
set2 = set(range(min(c, d), max(c, d) + 1))
e = (set1 & set2)
print(len(list(e)))
