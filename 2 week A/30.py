A = int(input())
B = int(input())
C = int(input())
R = max(A, B, C)
R2 = min(A, B, C)
R1 = A + B + C - (R + R2)
if A == B == C:
    print('acute')
elif R > R2 and R > R1:
    if R >= R1 + R2:
        print('impossible')
    elif R2*R2 + R1*R1 - R*R > 0:
        print('acute')
    elif R2*R2 + R1*R1 - R*R < 0:
        print('obtuse')
    elif R2*R2 + R1*R1 - R*R == 0:
        print('rectangular')
else:
    pass
