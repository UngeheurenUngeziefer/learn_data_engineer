l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())
if 0 <= l1 < r1 <= 100 and 0 <= l2 < r2 <= 100 and 0 <= l3 < r3 <= 100:
    if (l1 <= r2 and l2 <= r1 and l2 <= r3 and l3 <= r2)\
            or (l2 <= r1 and l1 <= r2 and l1 <= r3 and l3 <= r1)\
            or (l2 <= r3 and l3 <= r2 and l3 <= r1 and l1 <= r3)\
            or (l3 <= r2 and l2 <= r3 and l2 <= r1 and l1 <= r2)\
            or (l3 <= r1 and l1 <= r3 and l1 <= r2 and l2 <= r1)\
            or (l1 <= r2 and l3 <= r1 and l3 <= r2 and l2 <= r3):
        print(0)
    else:
        d1 = r1 - l1
        d2 = r2 - l2
        d3 = r3 - l3
        if (l3 > r2 and d1 >= l3 - r2)\
                or (l2 > r3 and d1 >= l2 - r3)\
                or (l2 <= r3 and l3 <= r2):
            print(1)
        elif (l3 > r1 and d2 >= l3 - r1)\
                or (l1 > r3 and d2 >= l1 - r3)\
                or (l1 <= r3 and l3 <= r1):
            print(2)
        elif (l1 > r2 and d3 >= l1 - r2)\
                or (l2 > r1 and d3 >= l2 - r1)\
                or (l1 <= r2 and l2 <= r1):
            print(3)
        else:
            print(-1)
else:
    print(-1)
