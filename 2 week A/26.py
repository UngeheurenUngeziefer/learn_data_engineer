M = int(input())
N = int(input())
K = int(input())

Square = N * M
if (K < Square) and (K % M == 0 or K % N == 0):
    print('YES')
else:
    print('NO')
