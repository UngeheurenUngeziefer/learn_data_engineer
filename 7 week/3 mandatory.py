flist = list(map(int, input().split()))
fset = set()
for i in flist:
    if i in fset:
        print('YES')
    else:
        print('NO')
    fset.add(i)
