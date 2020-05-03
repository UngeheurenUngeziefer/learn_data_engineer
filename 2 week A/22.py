
x = int(input())
xb = -1
steps = 0
r = 0
while x != 0:
    x = int(input())
    if xb == x:
        steps += 1
    else:
        xb = x
        r = max(r, steps)
        steps = 1
r = max(r, steps)
print(r)
