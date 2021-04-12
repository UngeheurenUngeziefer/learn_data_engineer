class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method - is a function inside of a class
    def bark(self):
        print('bark!')

    def meow(self, x):
        return 'meow ' * x

    def get_name(self):
        return self.name

    # getter
    def get_age(self):
        return self.age

    # setter
    def set_age(self, new_age):
        self.age = new_age

Tim = Dog('Tim', 2)
Bill = Dog('Bill', 5)

print(Bill.get_age())
