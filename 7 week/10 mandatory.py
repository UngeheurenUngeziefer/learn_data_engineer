# подгружаем какую то библиотеку позволяющую
# получать второе значение из кортежа
from operator import itemgetter

with open('input.txt') as f_input:
    data = f_input.read().split()
dictf = {}
counter = 1

# создаём словарь с значением и количеством упоминаний оного
for i in data:
    if i not in dictf:
        dictf[i] = counter
    else:
        dictf[i] += 1

# делаем из словаря кортеж, где ключ и значение
# равняется парам кортежа
items = list(dictf.items())

# сортируем кортеж по не возрастанию
p = sorted(sorted(items), key=lambda x: x[1], reverse=True)

# создаём список чтобы распечатать элементы каждый
# с новой строки
newlist = (list(map(itemgetter(0), p)))
sulist = newlist

# создаём цикл печатающий элементы списка с новой строки каждый
for i in sulist:
    print(i)
