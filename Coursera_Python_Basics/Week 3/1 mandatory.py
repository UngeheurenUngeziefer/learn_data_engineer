# Даны длины сторон треугольника. Вычислите площадь треугольника.
a = float(input())
b = float(input())
c = float(input())

p = (a + b + c)/2

S = p * (p - a) * (p - b) * (p - c)

print(S**0.5)
