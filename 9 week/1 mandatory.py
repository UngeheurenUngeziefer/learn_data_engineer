from sys import stdin
import copy


class Matrix(list):
    def __init__(self, m):
        self.m = copy.deepcopy(m)

    def __str__(self):
        return '\n'.join(['\t'.join([str(j) for j in i]) for i in self.m])

    def size(self):
        return len(self.m), len(self.m[0])

exec(stdin.read())
