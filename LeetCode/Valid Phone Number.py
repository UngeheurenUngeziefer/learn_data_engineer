f = open('file.txt', 'r')
number_list = []
for line in f:
    if line[0] == '(' and line[4] and line[5] == ' ' and line[9] == '-':
        number_list.append(line)
    elif line[3] == '-' and line[7] == '-':
        number_list.append(line)
print(number_list)
