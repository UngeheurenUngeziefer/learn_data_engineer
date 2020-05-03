A1 = int(input())
A2 = int(input())
B1 = int(input())
B2 = int(input())

if 1 > A1 > 8 or 1 > A2 > 8 or 1 > B1 > 8 or 1 > B2 > 8:
    print('NO')
elif (B1 == A1 + 1 or B1 == A1 - 1) and (B2 == A2 + 1 or B2 == A2 - 1):
    print('YES')
elif (B1 == A1) and (B2 == A2 + 1 or B2 == A2 - 1):
    print('YES')
elif (B2 == A2) and (B1 == A1 + 1 or B1 == A1 - 1):
    print('YES')
else:
    print('NO')
