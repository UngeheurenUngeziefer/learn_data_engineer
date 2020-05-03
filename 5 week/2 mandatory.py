A = int(input())
B = int(input())

if A < B:
    for i in range(A, B + 1):
        print(i)
elif A > B:
    for i in range(A, B - 1, -1):
        print(i)
elif A == B:
    print(A)
