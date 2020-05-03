S = input()
A = S.find('f')
B = S.rfind('f')
if A == -1:
    print()
elif A == B:
    print(A)
else:
    print(A, B)
