max = 0
n_max = 0
i = -1
while i != 0:
    i = int(input())
    if i > max:
        max, n_max = i, 1
    elif i == max:
        n_max += 1
print(n_max)
