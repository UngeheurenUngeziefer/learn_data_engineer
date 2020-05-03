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
