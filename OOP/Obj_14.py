class Math:
    # static method dont change anything
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def pr():
        print('run')

print(Math.add5(5))
Math.pr()

