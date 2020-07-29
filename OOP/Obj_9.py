from abc import ABC, abstractmethod


class Car:
    def __init__(self, color, year, newEngine):
        self.color = color
        self.year = year

        if issubclass(newEngine, Interface_of_engines):
            print('ok')
        else:
            print('error')

        self.engine = newEngine

    def startEngine(self):
        self.engine.on()

    def stopEngine(self):
        self.engine.off()

# интерфейс абстрактный метод, форма для других методов
class Interface_of_engines(ABC):
    @abstractmethod
    def on(self):
        pass
    # методы не реализуем
    @abstractmethod
    def off(self):
        pass


class Engine(Interface_of_engines):
    def on(self):
        # реализация
        pass

    def off(self):
        # реализация
        pass


class anotherEngine(Interface_of_engines):
    # реализация
    pass


engine = anotherEngine
myCar = Car('red', 2005, engine)
