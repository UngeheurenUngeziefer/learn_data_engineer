class Geek:
    def __init__(self, age=0):
        self._age = age

    # getter method
    def get_age(self):
        return self._age

    # setter method
    def set_age(self, x):
        self._age = x

Geek1 = Geek()
Geek1.age = 2
print(Geek1.get_age())
print(Geek1.set_age(2))
print(Geek1.get_age())
