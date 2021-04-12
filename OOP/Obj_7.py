class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # определяет поведение оператора ==
    def __eq__(self, other):
        return isinstance(other, Dog) and other.name == self.name

    # определяет поведение оператора +
    def __add__(self, other):
        return other.name + self.name

    # определяет поведение оператора неравенства
    def __ne__(self, other):
        if other.name != self.name:
            return 'objects not equal'
        else:
            return 'objects are equal'

    # определяет поведение оператора <
    def __lt__(self, other):
        if isinstance(other, Dog):
            return self.age < other.age

    # определяет поведение оператора >
    def __gt__(self, other):
        if isinstance(other, Dog):
            return self.age > other.age

    # определяет поведение оператора <=
    def __le__(self, other):
        if isinstance(other, Dog):
            return self.age <= other.age

    # определяет поведение оператора >=
        def __ge__(self, other):
            if isinstance(other, Dog):
                return self.age >= other.age

tim = Dog('Tim', 3)
joe = Dog('Joe', 3)

print(tim <= joe)
