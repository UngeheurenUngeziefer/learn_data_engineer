def inverse():
    n = int(input())
    if n != 0:
        inverse()
    print(n)


inverse()
