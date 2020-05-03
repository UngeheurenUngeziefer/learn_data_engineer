# Даны два натуральных числа n и m.
# Сократите дробь (n / m), то есть выведите два других числа p и q таких,
# что (n / m) = (p / q) и дробь (p / q) — несократимая.
# Решение оформите в виде функции ReduceFraction(n, m),
# получающая значения n и m и возвращающей кортеж из двух чисел: return p, q.
# Тогда вывод можно будет оформить как print(*ReduceFraction(n, m)).

n = int(input())
m = int(input())


def ReduceFraction(n, m):
    while n % 2 == 0 and m % 2 == 0:
        n = n // 2
        m = m // 2
    while n % 3 == 0 and m % 3 == 0:
        n = n // 3
        m = m // 3
    while n % 5 == 0 and m % 5 == 0:
        n = n // 5
        m = m // 5
    while n % 7 == 0 and m % 7 == 0:
        n = n // 7
        m = m // 7
    while n % 10 == 0 and m % 10 == 0:
        n = n // 10
        m = m // 10
    else:
        pass
    print(n, m)

ReduceFraction(n, m)
