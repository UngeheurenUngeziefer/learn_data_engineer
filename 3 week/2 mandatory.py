# (1 / 1²)+(1 / 2²)+(1 / 3²)+...+(1 / n²)

N = float(input())
X = 1
R = 0
S = 0

if N == X:
    print(1 / 1**2)
else:
    while N != X - 1:
        R = (1 / X**2)
        X += 1
        S += R
    print(S)
