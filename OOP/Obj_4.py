class Country:
    def __init__(self, flag, economy, region, language):
        self._flag = flag
        self._economy = economy
        self._region = region
        self._language = language

    # getter
    def get_flag(self):
        return self._flag

    # setter
    def set_flag(self, new_flag):
        self._flag = new_flag

Belarus = Country('red-green-white', 50, 'Eastern Europe', 'belarusian, russian')
print(Belarus.get_flag())
Belarus.set_flag('red-white-red')
print(Belarus.get_flag())