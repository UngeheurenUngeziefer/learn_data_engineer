# Дано три числа. Упорядочите их в порядке неубывания. Программа должна считывать три числа a,b,c,
# затем программа должна менять их значения так, чтобы стали выполнены условия a≤b≤c, затем программа выводит тройку
# a,b,c.

A, B, C = int(input()), int(input()), int(input())

if A >= B >= C:
    print(str(C) + ' ' + str(B) + ' ' + str(A))
elif B >= A >= C:
    print(str(C) + ' ' + str(A) + ' ' + str(B))
elif B >= C >= A:
    print(str(A) + ' ' + str(C) + ' ' + str(B))
elif C >= B >= A:
    print(str(A) + ' ' + str(B) + ' ' + str(C))
elif A >= C >= B:
    print(str(B) + ' ' + str(C) + ' ' + str(A))
elif C >= A >= B:
    print(str(B) + ' ' + str(A) + ' ' + str(C))
