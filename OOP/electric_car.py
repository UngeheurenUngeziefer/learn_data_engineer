# импортируем класс родитель
from car import Car

class Battery():
	'''Модель работы аккумулятора автомобиля'''
	def __init__(self, battery_size=80):
		'''Инициализирует атрибуты аккумулятора'''
		self.battery_size = battery_size

	def describe_battery(self):
		'''Выводит информацию о мощности аккумулятора'''
		print('This car has a ' + str(self.battery_size) + '-kWh battery.')

	def get_range(self):
		'''Выводит приблизительный запас хода аккумулятора'''
		if self.battery_size == 80:
			range_ = 250
		elif self.battery_size > 80:
			range_ = 300
		else:
			range_ = 200
		message = 'This car can go approximately ' + str(range_)
		message += ' miles on a full charge'
		print(message)

class ElectricCar(Car):
	'''Представляет специфические для электромашины аспекты'''
	def __init__(self, make, model, year):
		'''Инициализирует атрибуты класса-родителя
		Затем инициализирует специфические для электромобиля атрибуты'''
		super().__init__(make, model, year)
		self.battery = Battery()

	def fill_gas_tank(self):
		'''Электромобили не нуждаются в заправке'''
		print('This car has no gas bank!')

# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.fill_gas_tank()
# my_tesla.battery.get_range()
