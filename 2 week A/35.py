k = int(input())
m = int(input())
n = int(input())

if n <= k:
    r = 2 * m
elif n * 2 % k == 0:
    r = m * (n * 2 // k)
else:
    r = m * (1 + (n * 2 // k))
print(r)
