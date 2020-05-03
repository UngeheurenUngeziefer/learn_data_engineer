h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

N1 = (h2 - h1) * 3600
N2 = (m2 - m1) * 60
N3 = (s2 - s1)

print(N1 + N2 + N3)
