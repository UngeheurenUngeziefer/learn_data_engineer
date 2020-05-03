# Найдите наибольшее значение в списке и индекс последнего элемента, который имеет данное значение за один проход
# по списку, не модифицируя этот список и не используя дополнительного списка.
# Выведите два значения.

lst = list(map(int, input().split()))

greater = lst[0]
gindex = 0
for i, v in enumerate(lst):
    if v >= greater:
        gindex = i
        greater = v
print(greater, gindex)
