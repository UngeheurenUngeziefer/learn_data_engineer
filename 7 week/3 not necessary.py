# Входные данные:
# 10
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

n = int(input())
setn = set(range(1, n + 1))
while True:
    flist = input()
    if flist == 'HELP':
        break
    flist = {int(x) for x in flist.split()}
    if len(set(flist) & setn) > len(setn)/2:
        print('YES')
        setn &= flist
    else:
        print('NO')
        setn -= flist

print(*sorted(setn))
