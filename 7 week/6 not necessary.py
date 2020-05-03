s = input()
fnum = input()
snum = input()
tnum = input()
dictnum = {}
slist = (fnum, snum, tnum)
flist = []
for i in slist:
    i = i.replace('-', '')
    i = i.replace('+', '')
    i = i.replace(')', '')
    i = i.replace('(', '')
    if len(i) == 7:
        i = '495' + i
    elif len(i) == 11:
        i = i[1:]
    flist.append(i)

s = s.replace('-', '')
s = s.replace('+', '')
s = s.replace(')', '')
s = s.replace('(', '')
if len(s) == 7:
    s = '495' + s
elif len(s) == 11:
    s = s[1:]

for i in flist:
    if s == i:
        print('YES')
    else:
        print('NO')
