P = int(input())  # процент
X = int(input())
Y = int(input())  # копейки

XR = X * 100   # рубли в копейках
Summ = XR + Y
Fin = Summ + (Summ * P / 100)

A = Fin / 100
B = Fin % 100
print(str(int(A)) + ' ' + str(int(B)))
