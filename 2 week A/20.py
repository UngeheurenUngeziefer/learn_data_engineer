n = int(input())
che = 0
step = 0
while n != 0:
    if n % 2 == 0:
        che += n
        step += 1
    n = int(input())
print(step)
