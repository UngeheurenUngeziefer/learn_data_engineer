text = input()

part1 = text[0:2]
part2 = text[2:4]
s = 0
r = part2[::-1]

if len(text) == 4 and part1 == r:
    print('1')
elif len(text) == 1 and int(text) == 0:
    print('1')
elif len(text) == 2 and int(text) == 00:
    print('1')
elif len(text) == 3 and text[2] == '0' and text[0] == text[1]:
    print('1')
else:
    print('5')
