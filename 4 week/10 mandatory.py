# Дана последовательность чисел, завершающаяся числом 0. Найдите сумму всех этих чисел, не используя цикл.

def countline():
    n = int(input())
    if n == 0:
        return 0
    return n + countline()


print(countline())
