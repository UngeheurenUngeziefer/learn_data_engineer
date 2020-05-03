l1 = int(input())
w1 = int(input())
h1 = int(input())

l2 = int(input())
w2 = int(input())
h2 = int(input())

lc = int(input())
wc = int(input())
hc = int(input())

lmax = max(l1, l2)
lmin = min(l1, l2)
hmax = max(h1, h2)

if (((lc >= l1 + l2 or wc >= w1 + w2 or wc >= l1
      + l2 or lc >= w1 + w2) and hc >= hmax) and l1
        + l2 < lc or w1 + w2 < wc):
    print('YES')
elif (((lc >= l1 + l2 or wc >= w1 + w2 or wc >= l1
        + l2 or lc >= w1 + w2) and hc >= hmax) and l1
      + l2 < lc or w1 + w2 < wc):
    print('YES')
elif ((((lc > l1 and lc > l2) or (wc > w1 and wc > w2) or (lc > l1 and lc > l2)) and hc >= hmax) and l1
      + l2 < lc or w1 + w2 < wc):
    print('YES')
else:
    print('NO')
