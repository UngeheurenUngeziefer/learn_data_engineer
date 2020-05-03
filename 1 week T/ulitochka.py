X = int(input())
A = int(input())
B = int(input())
dist = 0
days = 0

while True:
    dist += A
    days += 1
    if dist >= X:
        break
    dist -= B
print(days)
