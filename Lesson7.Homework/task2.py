from abc import ABC, abstractmethod


class AbstractRule(ABC):
    @abstractmethod
    def cloth_consume(self, param):
        pass


class Cloth(AbstractRule):
    _total_consume = 0

    def __init__(self, name: str):
        self.name = name

    def cloth_consume(self, count_cloth: float):
        print(f'Расходую {count_cloth} ткани на другую одежду')
        Cloth._total_consume += count_cloth
        return count_cloth

    @staticmethod
    def total_consume():
        return f'Общий расход: {Cloth._total_consume}'


class Coat(Cloth):

    def __init__(self, name: str, size: float):
        self.name = name
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 0:
            print('Размер не может быть меньше нуля')
        else:
            self.__size = size

    def cloth_consume(self, count: int):
        consume = (self.size / 6.5 + 0.5) * count
        print(f'На создание пальто: "{self.name}" израсходано {consume} ткани')
        Cloth._total_consume += consume
        return consume


class Suite(Cloth):
    def __init__(self, name: str, growth: float):
        self.name = name
        self.growth = growth

    @property
    def growth(self):
        return self.__growth

    @growth.setter
    def growth(self, growth):
        if growth < 0:
            print('Рост не может быть меньше нуля')
        else:
            self.__growth = growth

    def cloth_consume(self, count: int):
        consume = (2 * self.growth + 0.3) * count
        print(f'На создание костюма: "{self.name}" израсходано {consume} ткани')
        Cloth._total_consume += consume
        return consume


suite = Suite('Костюм артиста', 45)
cloth = Cloth('Одежда для собаки')
coat = Coat('Пальто незнакомца', 170)
suite.cloth_consume(10)
print(Cloth.total_consume())
coat.cloth_consume(10)
print(Cloth.total_consume())
cloth.cloth_consume(500)
print(Cloth.total_consume())
