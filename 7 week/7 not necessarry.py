n = int(input())
councity = {}
for i in range(n):
    country, *cities = input().split()
    for city in cities:
        councity[city] = country
n2 = int(input())
for name in range(n2):
    city2 = input()
    print(councity[city2])
