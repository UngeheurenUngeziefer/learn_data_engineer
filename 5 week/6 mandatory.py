# Выведите все четные элементы списка.
numList = list(map(int, input().split()))
newlist = ()

for i in numList:
    if i % 2 == 0:
        newlist = (*newlist, i)
print(*newlist, sep=' ')
