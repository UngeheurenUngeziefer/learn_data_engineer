n = int(input())


def IsPrime(n):
    num = 1
    if n == 1 or n <= 0:
        print('NO')
    elif n > 1:
        for i in range(2, (int(n ** 0.5)) + 1):
            if n % i == 0:
                num += 1
            else:
                pass
        if num > 1:
            print('NO')
        else:
            print('YES')


IsPrime(n)
