a = list(map(int, input().split()))

fir = a.index(max(a))
sec = a.index(min(a))

a[fir], a[sec] = a[sec], a[fir]
print(*a, sep=' ')
