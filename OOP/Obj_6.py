class IsNumsEqual():
    def __init__(self, first_num, second_num):
        self._first_num = first_num
        self._second_num = second_num


x = [1]
y = [1]

print(x is y)
print(x == y)


print(id(x))
print(id(y))

