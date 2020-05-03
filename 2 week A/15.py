X = int(input())
Y = int(input())

days = 1
while X < Y:
    X += X/10
    days += 1
print(days)
