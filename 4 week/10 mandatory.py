def countline():
    n = int(input())
    if n == 0:
        return 0
    return n + countline()


print(countline())
