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
    return (-man.point, man.name)
a.sort(key=make_tuple)

for now in a:
    print(now.name)
