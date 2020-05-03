x = float(input())      # координаты
y = float(input())      # координаты
xc = float(input())     # координаты центра круга
yc = float(input())     # координаты центра круга
r = float(input())      # радиус


def ispointincircle(x, y, xc, yc, r):
    return (y - yc)**2 + (x - xc)**2 <= r**2


if ispointincircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
