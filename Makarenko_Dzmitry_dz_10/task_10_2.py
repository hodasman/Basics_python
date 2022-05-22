"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность этого проекта — одежда (class Clothes).
К типам одежды в этом проекте относятся пальто (class Coat) и костюм (class Costume).
У этих типов одежды существуют параметры: размер size (для пальто) и рост height (для костюма).
Значения параметров size и height, которые они могут принять предусмотреть как float.

Для определения расхода ткани по каждому типу одежды использовать формулы:

для пальто (size / 6.5 + 0.5),
для костюма (2 * height + 0.3),
расчёты расхода ткани производить в методе calculate, который должен возвращать float-значение с количеством знаков
после плавающей точки не более двух
Оформить код, используя декоратор абстрактного метода, чтобы регламентировать обязательное
определение в классах типов одежды метода calculate. Используйте декоратор @property для возможности обращения
к методу calculate, как к атрибуту класса.
"""

from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def calculate(self):
        pass

class Coat(Clothes):
    def __init__(self, size: float):
        self.size = size

    @property
    def calculate(self):
        return float("{0:.2f}".format(self.size / 6.5 + 0.5))


class Costume(Clothes):
    def __init__(self, height: float):
        self.height = height

    @property
    def calculate(self):
        return float("{0:.2f}".format(self.height * 2 + 0.3))

if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)

    print(coat.calculate)  # 7.42
    print(costume.calculate)  # 6.3