# Даны три целых числа A, B, C. Определить, есть ли среди них хотя бы одно четное и хотя бы одно нечетное.
N1 = int(input())
N2 = int(input())
N3 = int(input())

if N1 % 2 == 0 and N2 % 2 == 0 and N3 % 2 != 0 or\
        N1 % 2 == 0 and N2 % 2 != 0 and N3 % 2 == 0 or\
        N1 % 2 != 0 and N2 % 2 == 0 and N3 % 2 == 0 or\
        N1 % 2 != 0 and N2 % 2 != 0 and N3 % 2 == 0 or\
        N1 % 2 == 0 and N2 % 2 != 0 and N3 % 2 != 0 or\
        N1 % 2 != 0 and N2 % 2 == 0 and N3 % 2 != 0:
    print('YES')
else:
    print('NO')
