z = int(input())
a = [int(i) for i in input().split()]
b = int(input())
lst = []

for i in a:
    r = b - i
    if r == 0:
        print(i)
        exit()
    elif r < 0:
        lst.append(-r)
    elif r > 0:
        lst.append(r)

s = lst.index(min(lst))
print(a[s])
