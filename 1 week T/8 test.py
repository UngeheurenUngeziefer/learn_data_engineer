v = int(input())    # км в час
t = int(input())    # прошло часов
k = v*t
while k >= 109:        # k заходит в значение меньше 108
    k -= 109
while k < 0:
    k += 109        # k заходит в значение больше 0
else:
    print(k)
