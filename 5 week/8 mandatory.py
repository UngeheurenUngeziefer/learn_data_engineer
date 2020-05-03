lst = list(map(int, input().split()))

greater = lst[0]
gindex = 0
for i, v in enumerate(lst):
    if v >= greater:
        gindex = i
        greater = v
print(greater, gindex)
