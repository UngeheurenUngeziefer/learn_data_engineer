# В кафе мороженое продают по три шарика и по пять шариков. Можно ли купить ровно k шариков мороженого?
N = int(input())
if N % 3 == 0:
    print('YES')
elif N % 5 == 0:
    print('YES')
elif N % 8 == 0:
    print('YES')
elif N > 10:
    print('YES')
else:
    print('NO')
