A = list(map(int, input().split()))
N = max(A)

B = [0] * (N + 1)
for i in A:
    B[i] = B[i] + 1
for j in range(N + 1):
    print((str(j) + ' ') * B[j], end='')
