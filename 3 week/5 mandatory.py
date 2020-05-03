import math
N = float(input())

if N - int(N) == 0.5:
    print(math.ceil(N))
else:
    print(round(N))
