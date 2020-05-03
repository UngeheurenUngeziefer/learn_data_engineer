from sys import stdin
import copy


class Matrix(list):
    def __init__(self, m):
        self.m = copy.deepcopy(m)

    def __str__(self):
        return '\n'.join(['\t'.join([str(j) for j in i]) for i in self.m])

    def size(self):
        return len(self.m), len(self.m[0])

    def __add__(self, other):
        res = Matrix
        res.m = []
        for i in range(len(self.m)):
            temp = []
            for j in range(len(self.m[0])):
                x = self.m[i][j] + other.m[i][j]
                temp.append(x)
            res.m.append(temp)
        return Matrix(res.m)

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

    __rmul__ = __mul__

exec(stdin.read())
