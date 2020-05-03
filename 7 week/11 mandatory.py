# подгружаем какую то библиотеку позволяющую
# получать второе значение из кортежа
from operator import itemgetter

with open('input.txt', mode='r', encoding='utf-8') as f_input:
    data = f_input.read().splitlines()
dictf = {}
counter = 1


# создаём словарь с значением и количеством
# упоминаний оного
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
# создаём список чтобы распечатать
# элементы каждый с новой строки
newlist = (list(map(itemgetter(0), p)))
# считаем количество голосов - уникальных строк


count = [lis[1] for lis in items]
summ = sum(count)
# вводим значение половина количества голосов
fifty = summ // 2

file = open("output.txt", "w", encoding='utf8')


# если больше половины печатаем его
# если никто не набрал больше половины печатаем первых двух
if p[0][1] > fifty:
    first = p[0][0]
    file.write(first)

elif p[0][1] <= fifty:
    second = p[0][0]
    third = p[1][0]
    lines = [second, third]
    with open("output.txt", "w", encoding='utf-8') as file:
        for line in lines:
            file.write(line + '\n')
file.close()
f_input.close()
