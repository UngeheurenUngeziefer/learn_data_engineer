# В олимпиаде участвовало N человек. Каждый получил определенное количество баллов, при этом оказалось, что у всех
# участников разное число баллов. Упорядочите список участников олимпиады в порядке убывания набранных баллов.
# Программа получает на вход число участников олимпиады N. Далее идет N строк, в каждой строке записана фамилия
# участника, затем, через пробел, набранное им количество баллов.

class Man:
    name = ''
    point = 0

a = []
n = int(input())

for i in range(n):
    name, point = input().split()
    point = int(point)
    man = Man()
    man.name = name
    man.point = point
    a.append(man)


def make_tuple(man):
    return -man.point, man.name
a.sort(key=make_tuple)

for now in a:
    print(now.name)
