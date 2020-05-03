A1 = int(input())
A2 = int(input())
B1 = int(input())
B2 = int(input())

if (A1 + A2) % 2 == 0 and (B1 + B2) % 2 == 0:
    print('YES')
elif (A1 + A2) % 2 != 0 and (B1 + B2) % 2 != 0:
    print('YES')
else:
    print('NO')
