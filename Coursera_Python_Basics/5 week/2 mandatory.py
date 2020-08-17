# Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания,если A < B,
# или в порядке убывания в противном случае.
A = int(input())
B = int(input())

if A < B:
    for i in range(A, B + 1):
        print(i)
elif A > B:
    for i in range(A, B - 1, -1):
        print(i)
elif A == B:
    print(A)
