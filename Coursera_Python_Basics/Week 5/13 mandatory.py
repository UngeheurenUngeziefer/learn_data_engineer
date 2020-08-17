# В списке все элементы попарно различны.
# Поменяйте местами минимальный и максимальный элемент этого списка.

a = list(map(int, input().split()))

fir = a.index(max(a))
sec = a.index(min(a))

a[fir], a[sec] = a[sec], a[fir]
print(*a, sep=' ')
