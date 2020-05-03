# Известно, что фамилии всех участников — различны. Сохраните в массивах список всех участников и выведите его,
# отсортировав по фамилии в лексикографическом порядке. При выводе указываете фамилию, имя участника и его балл.
# Используйте для ввода и вывода файлы input.txt и output.txt с указанием кодировки utf8. Например, для чтения откройте
# файл с помощью open('input.txt', 'r', encoding='utf8').

f = open('input.txt', 'r', encoding='utf8')
a = []
for i in f:
    a.append(i.split())
f.close()

a.sort()

outFile = open('output.txt', 'w', encoding='utf8')
for line in a:
    line = [line[0], line[1], line[-1]]
    print(' '.join(map(str, line)), end='\n', file=outFile)
outFile.close()
