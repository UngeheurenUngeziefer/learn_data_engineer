a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = a + b

list.sort(c)
print(*c)
