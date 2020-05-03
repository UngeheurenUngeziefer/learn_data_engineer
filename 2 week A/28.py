X1 = int(input())
Y1 = int(input())
X2 = int(input())
Y2 = int(input())

if X1 > 0 and X2 > 0:
    if Y1 > 0 and Y2 > 0:
        print('YES')
    elif Y1 < 0 and Y2 < 0:
        print('YES')
    else:
        print('NO')
elif X1 < 0 and X2 < 0:
    if Y1 > 0 and Y2 > 0:
        print('YES')
    elif Y1 < 0 and Y2 < 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
