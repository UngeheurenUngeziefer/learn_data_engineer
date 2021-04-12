class Dog():
	'''initialization of the dog class with age and name fields'''
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def roll_over(self):
		# dog rolling func
		return 'The Dog ' + self.name + ' rolling.'

	def bark(self):
		# dog barking func
		return 'The Dog ' + self.name + ' barking'

	def age_is(self):
		# func display age of the dog
		return self.name + ' age is ' + str(self.age)

Sussie = Dog('Sussie', 2)
print(Sussie.roll_over())

Marty = Dog('Marty', 1)
print(Marty.bark())

Sasha = Dog('Sasha', 3)
print(Sasha.age_is())