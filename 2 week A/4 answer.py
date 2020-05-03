A = int(input())
R = A % 100
if A % 4 == 0 and R != 0 or A % 400 == 0:
    print('YES')
else:
    print('NO')
