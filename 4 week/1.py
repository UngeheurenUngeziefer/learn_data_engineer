x = float(input())
y = float(input())


def ispointinsquare(x, y):
    r = x + y
    return -1 <= r <= 1
ispointinsquare(x, y)


if ispointinsquare(x, y):
    print('YES')
else:
    print('NO')
