# 3 or 5
N = int(input())
if N % 3 == 0:
    print('YES')
elif N % 5 == 0:
    print('YES')
elif N % 8 == 0:
    print('YES')
elif N > 10:
    print('YES')
else:
    print('NO')
