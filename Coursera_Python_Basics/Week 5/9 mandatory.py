# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

a = [int(i) for i in input().split()]
lst = []
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        lst.append(a[i])

print(*lst, sep=' ')
