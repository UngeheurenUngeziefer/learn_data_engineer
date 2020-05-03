N = int(input())


while int(N) in range(1440, 100000001):
    N = (N-int(1440))
else:
    pass

X1 = N//int(60)
XR = N % int(60)


def zero_hour():
    if N in range(0, 60):
        print('0 ' + str(N))


zero_hour()


def other_hours():
    if N in range(60, 1440):
        print(str(X1) + ' ' + str(XR))


other_hours()
