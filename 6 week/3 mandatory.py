n = list(map(int, input().split()))
b = []
for i in range(n[1]):
    b.append(int(input()))

b.sort()
d, c = 0, 0
for i in b:
    d += i
    if d <= n[0]:
        c += 1
print(c)
