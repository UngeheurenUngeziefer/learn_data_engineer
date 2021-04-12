# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
a = int(input())
b = int(input())


def sum(a, b):
    if b > a:
        for i in range(0, a):
            b += 1
        print(b)
    elif b == a:
        for i in range(0, a):
            b += 1
        print(b)
    elif b < a:
        for i in range(0, b):
            a += 1
        print(a)


sum(a, b)
