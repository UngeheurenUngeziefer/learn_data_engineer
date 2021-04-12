class Human():
    def __init__(self, gender, age, race, country):
        self.garbage = 102938
        self._gender = gender
        self._age = age
        self._race = race
        self._country = country

    def __del__(self):
        self.garbage = self._age
        del self.garbage

Anna = Human('woman', 42, 'white', 'Sweden')
print(Anna._gender, Anna._age, Anna.garbage)

Anna.__del__()
print(Anna._gender, Anna._age)
