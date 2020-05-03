v = int(input())
t = int(input())

x = v*t

while x > 108:
    x -= 109

if v < 0:
    print(109 + x)
else:
    print(x)
