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
