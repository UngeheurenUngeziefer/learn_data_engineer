a = int(input())
b = list(map(int, input().split()))

list.sort(b)

print(*b)
