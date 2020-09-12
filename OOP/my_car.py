from car import Car
from electric_car import ElectricCar

Beetle = Car('Volkswagen', 'Beetle', 2016)
print(Beetle.get_descriptive_name())
Tesla = ElectricCar('Tesla', 'Roadster', 2016)
print(Tesla.get_descriptive_name())
