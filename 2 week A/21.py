b = int(input())
max1 = b
a = int(input())
max2 = a
if max1 < max2:
    d = max1
    max1 = max2
    max2 = d
while a != 0:
    a = int(input())
    if max1 < a:
        max2 = max1
        max1 = a
    elif max2 < a <= max1:
        max2 = a
print(max2)
