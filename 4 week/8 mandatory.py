a = float(input())
n = float(input())


def func(a, n):
    if n == 1:
        print(a)
    elif n % 2 == 0:
        print((a ** 2) ** (n / 2))
    elif n % 2 != 0:
        print(a * (a ** (n - 1)))


func(a, n)
