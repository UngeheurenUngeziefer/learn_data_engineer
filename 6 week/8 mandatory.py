inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
z = int(inFile.readline())
a = []

for line in inFile:
    newLine = line.split()
    if int(newLine[-1]) >= 40 and int(newLine[-2]) >= 40 \
            and int(newLine[-3]) >= 40:
        a.append(newLine)
a.sort(key=lambda b: int(b[-1]) + int(b[-2]) + int(b[-3]))
a.reverse()
konk = []


for i in a:
    sum = int(i[-1]) + int(i[-2]) + int(i[-3])
    konk.append(sum)
n = len(konk)


def konkurs(n, z, konk):
    if n <= z:
        return 0
    elif konk[z] == konk[0]:
        return 1
    for i in range(z, 0, -1):
        if konk[i] < konk[i - 1]:
            return konk[i - 1]

print(konkurs(n, z, konk), file=outFile)

inFile.close()
outFile.close()
