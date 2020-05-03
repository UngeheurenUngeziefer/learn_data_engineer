A = int(input())
B = int(input())

R = B - A
R1 = B - A + 1  # num of apartm in range
R2 = B - R - 1   # apartm remained
R3 = R2 / R1

if R + 1 != R1:
    print('NO')
elif B > 0 and A > 0 and R == 0:
    print('YES')
elif R2 % R1 == 0:
    print('YES')
else:
    print('NO')
