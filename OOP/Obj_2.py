class Car:
    def __init__(self, color, year, manufacturer):
        self._color = color
        self._year = year
        self._manufacturer = manufacturer

    # getter
    def display_color(self):
        return self._color

    # setter
    def change_color(self, color):
        if isinstance(color, str):
            self._color = color
        else:
            print('Color must be string!')




# создаём объект с определёнными параметрами
myCar = Car
myCar.color = 'red'
myCar.year = 2007
myCar.manufacturer = 'Mercedes'
print(myCar.color, myCar.year, myCar.manufacturer)

# меняем одно из свойств объекта
myCar.color = 'blue'
print(myCar.color)

# меняем свойство объекта с помощью функции
myCar.change_color(myCar, 'purple')
print(myCar.color)

# покажем цвет
print(myCar.display_color(myCar))

