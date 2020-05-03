l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())

maxl = max(l1, l2, l3)
minl = min(l1, l2, l3)
midl = (l1 + l2 + l3) - (minl + maxl)
maxr = max(r1, r2, r3)
minr = min(r1, r2, r3)
midr = (r1 + r2 + r3) - (minr + maxr)

# переменные длины спичек
flen = r1 - l1
slen = r2 - l2
tlen = r3 - l3

# если пересекаются все то пропишем ответ 0
if minr >= midl and maxl <= midr:
    print(0)
# если спичка больше или равна чем расстояние между двумя другими
elif r3 > r2 and flen >= l3 - r2:
    print(1)
elif r3 < r2 and flen >= l2 - r3:
    print(1)
elif r3 > r1 and slen >= l3 - r1:
    print(2)
elif r3 < r1 and slen >= l1 - r3:
    print(2)
elif r1 > r2 and tlen >= l1 - r2:
    print(3)
elif r2 > r1 and tlen >= l2 - r1:
    print(3)

# noone
elif r1 < l2 and r2 < l3 and r3 - l3 < l2 - r1 and r1 - l1 < l3 - r2:
    print(-1)
elif r1 < l3 and r3 < l2 and r2 - l2 < l3 - r1 and r1 - l1 < l2 - r3:
    print(-1)
elif r3 < l2 and r2 < l1 and r1 - l1 < l2 - r3 and r3 - l3 < l1 - r2:
    print(-1)
elif r3 < l1 and r1 < l2 and r2 - l2 < l1 - r3 and r3 - l3 < l2 - r1:
    print(-1)
elif r2 < l1 and r1 < l3 and r3 - l3 < l1 - r2 and r2 - l2 < l3 - r1:
    print(-1)
elif r2 < l3 and r3 < l1 and r1 - l1 < l3 - r2 and r2 - l2 < l1 - r3:
    print(-1)

# touch12
elif (r1 >= l2 or (l2 > l1 and r2 < r1) or (l1 > l2 and r1 < r2))\
        and (l3 > r2 and l3 > l2):
    print(3)
elif (r1 >= l3 or (l3 > l1 and r3 < r1) or (l1 > l3 and r1 < r3)) \
        or (l2 > r3 and l2 > l3):
    print(2)
# touch23
elif (r2 >= l3 or (l3 > l2 and r3 < r2) or (l2 > l3 and r2 < r3)) \
        and (l1 > r3 and l1 > l3):
    print(1)
else:
    print(0)
