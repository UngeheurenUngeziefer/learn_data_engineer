class Word(str):
    """Класс для слов, определяющий сравнение по длине слов."""

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)

cat = Word('cat')
dog = Word('dog')

print(cat >= dog)

