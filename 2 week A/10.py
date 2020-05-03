A = int(input())
B = int(input())
C = int(input())

if A == B == C:
    print('3')
elif A == B or A == C or B == C:
    print('2')
elif A != B and A != C and B != C:
    print('0')
