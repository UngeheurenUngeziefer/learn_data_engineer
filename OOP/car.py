class Car():
	'''Простая модель автомобиля'''
	def __init__(self, make, model, year):
		'''Инициализирует атрибуты описания автомобиля'''
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		'''Возвращает аккуратно отформатированное описание'''
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		'''Выводит пробег машины в милях'''
		print('This car has ' + str(self.odometer_reading) + ' miles on it.')

	def update_odometer(self, mileage):
		'''Устанавливает обновлённое значение одометра
		При откате значение не меняется'''
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, mileage):
		'''Увеличивает значение одометра на заданный показатель'''
		if mileage >= 0:
			self.odometer_reading += mileage
		else:
			print("You can't roll back an odometer!")

# my_new_car = Car('Audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
# my_new_car.update_odometer(24)
# my_new_car.read_odometer()
# my_new_car.update_odometer(20)
# my_new_car.increment_odometer(-20)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(20)
# my_new_car.read_odometer()