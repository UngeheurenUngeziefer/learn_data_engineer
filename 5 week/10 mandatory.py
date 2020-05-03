a = [int(i) for i in input().split()]
lst = []
for i in a:
    if i > 0:
        lst.append(i)

print(min(lst))
