# Добавьте в программу из предыдущей задачи класс MatrixError,
# содержащий внутри self поля matrix1 и matrix2 — ссылки на матрицы.
# В класс Matrix внесите следующие изменения:
# Добавьте в метод __add__ проверку на ошибки в размере входных данных, чтобы при попытке сложить матрицы разных
# размеров было выброшено исключение MatrixError таким образом, чтобы matrix1 поле MatrixError
# стало первым аргументом __add__ (просто self), а matrix2 — вторым (второй операнд для сложения).
# Реализуйте метод transpose, транспонирующий матрицу и возвращающую результат
# (данный метод модифицирует экземпляр класса Matrix)
# Реализуйте статический метод transposed, принимающий Matrix и возвращающий транспонированную матрицу.
# Пример статического метода.

from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other


class Matrix(list):
    def __init__(self, m):
        self.m = copy.deepcopy(m)

    def __str__(self):
        return '\n'.join(['\t'.join([str(j) for j in i]) for i in self.m])

    def size(self):
        return len(self.m), len(self.m[0])

    def __add__(self, other):
        if len(self.m) == len(other.m):
            lenght = len(self.m[0])
            for row in self.m:
                if len(row) != lenght:
                    raise MatrixError(self, other)
            for row2 in other.m:
                if len(row2) != lenght:
                    raise MatrixError(self, other)
            result = []
            numbers = []
            for i in range(len(self.m)):
                for j in range(len(self.m[0])):
                    summa = other.m[i][j] + self.m[i][j]
                    numbers.append(summa)
                    if len(numbers) == len(self.m[0]):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        newl = Matrix
        newl.m = []
        for i in range(len(self.m)):
            temp = []
            for j in range(len(self.m[0])):
                x = self.m[i][j] * other
                temp.append(x)
            newl.m.append(temp)
        return Matrix(newl.m)

    def transpose(self):
        tmatrix = list(zip(*self.m))
        self.m = tmatrix
        return Matrix(tmatrix)

    def transposed(self):
        tmatrix = list(zip(*self.m))
        return Matrix(tmatrix)

    __rmul__ = __mul__

exec(stdin.read())
