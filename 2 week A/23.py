x = int(input())
m = 0
steps = 0
x = -1
while x != 0:
    x = int(input())
    if x > m:
        m, steps = x, 1
    elif x == m:
        steps += 1
print(steps)
