# За многие годы заточения узник замка Иф проделал в стене прямоугольное отверстие размером D×E.
# Замок Иф сложен из кирпичей, размером A×B×C. Определите, сможет ли узник выбрасывать кирпичи
# в море через это отверстие (очевидно, стороны кирпича должны быть параллельны сторонам отверстия).

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a <= d and b <= e or a <= e and b <= d:
    print("YES")
elif c <= d and b <= e or c <= e and b <= d:
    print("YES")
elif a <= d and c <= e or a <= e and c <= d:
    print("YES")
else:
    print("NO")
