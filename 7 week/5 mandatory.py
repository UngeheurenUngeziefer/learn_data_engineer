# Входные данные:
# 10
# 1 2 3 4 5
# YES
# 2 4 6 8 10
# NO
# HELP
#
# Вывод программы:
# 1 3 5
n = int(input())
setn = set(range(1, n + 1))
while True:
    flist = input()
    if flist == 'HELP':
        break
    flist = {int(x) for x in flist.split()}
    s1 = input()
    if s1 == 'YES':
        setn &= flist
    elif s1 == 'NO':
        setn -= flist
print(*sorted(setn))
