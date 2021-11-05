from abc import ABC, abstractmethod


class Сlothes(ABC):
    name: str
    result = 0

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def calculate(self):
        pass

    def __add__(self, other):
        Сlothes.result = self.calculate() + other.calculate
        return

    def __str__(self):
        tmp = Сlothes.result
        return tmp


class Сoat(Сlothes):
    _size: float

    def __init__(self, name: str, V: float):
        super().__init__(name)
        self.__V = V

    @property
    def calculate(self):
        return round(self.__V/6.5 + 0.5, 2)


class Suit(Сlothes):
    def __init__(self, name, H):
        super().__init__(name)
        self.__H = H

    @property
    def calculate(self):
        return round(2 * self.__H + 0.3, 2)


test_1 = Сoat("Пальто", 1)
test_2 = Suit(1)
print(test_1.calculate)
print(test_2.calculate)