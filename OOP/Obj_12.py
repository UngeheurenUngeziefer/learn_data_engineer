# Inheritance
# difference only in speak method
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def speak(self):
#         print('meow')
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def speak(self):
#         print('wow')

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and I am {self.color}')

    def speak(self):
        print('I dont know what I say')


class Cat(Pet):
    def __init__(self, name, age, color):
        # get init from super class Pet
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print('meow')

class Dog(Pet):
    def speak(self):
        print('wow')

class Fish(Pet):
    pass

Tim = Cat('Tim', 19, 'black')
Jill = Dog('Jill', 19)
Joe = Fish('Bubbles', 10)
Tim.show()
Jill.speak()
Joe.speak()
