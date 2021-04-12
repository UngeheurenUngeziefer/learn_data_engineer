# Заданы две клетки шахматной доски.
# Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета – то NO.
A1 = int(input())
A2 = int(input())
B1 = int(input())
B2 = int(input())

if (A1 + A2) % 2 == 0 and (B1 + B2) % 2 == 0:
    print('YES')
elif (A1 + A2) % 2 != 0 and (B1 + B2) % 2 != 0:
    print('YES')
else:
    print('NO')
