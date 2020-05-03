a, b, c = int(input()), int(input()), int(input())
x, y, z = int(input()), int(input()), int(input())
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y
if x > y:
    x, y = y, x
if a == x and b == y and c == z:
    print('Boxes are equal')
elif a <= x and b <= y and c <= z:
    print('The first box is smaller than the second one')
elif a >= x and b >= y and c >= z:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
