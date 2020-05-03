# Даны действительные коэффициенты a, b, c, при этом a != 0.
# Решите квадратное уравнение ax²+bx+c=0 и выведите все его корни.

a = float(input())  # a != 0
b = float(input())
c = float(input())

D = (b ** 2) - (4 * a * c)

if D < 0:
    pass
elif D == float(0):
    x1 = -1 * (b / (2 * a))
    print(float(x1))
elif D > 0:
    x1 = ((-1 * b) + (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)
    x2 = ((-1 * b) - (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)
    print(min(x1, x2), max(x1, x2))
