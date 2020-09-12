# импортируем класс родитель
from car import Car

class ElectricCar(Car):
	'''Представляет специфические для электромашины аспекты'''
	def __init__(self, make, model, year):
		'''Инициализирует атрибуты класса-родителя
		Затем инициализирует специфические для электромобиля атрибуты'''
		super().__init__(make, model, year)
		self.battery_size = 80

	def describe_battery(self):
		'''Выводит информацию о мощности аккумулятора'''
		print('This car has a ' + str(self.battery_size) + '-kWh battery.')

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
