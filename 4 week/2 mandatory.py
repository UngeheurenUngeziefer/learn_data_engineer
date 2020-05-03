x = float(input())
y = float(input())


def ispointinsquare(x, y):
    return 1 >= x >= -1 and 1 >= y >= -1
ispointinsquare(x, y)


if ispointinsquare(x, y):
    print('YES')
else:
    print('NO')
