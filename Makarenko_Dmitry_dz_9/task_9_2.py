"""
Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
проверить работу метода.
"""


class Road:
    def __init__(self, length: int, width: int):
        """конструктор класса
        :param length: длинна в метрах
        :param width: ширина в метрах
        """
        self._length = length
        self._width = width

    def calculate(self, height: int = 5, mass_m_2: int = 25) -> int:
        """
        считает масу массу асфальта, необходимого для покрытия всей дороги в тоннах
        :param height: высота дорожного полотна в сантиметрах
        :param mass_m_2: масса в кг квадратного метра дороги высотой 1 см
        :return: int значение тонн, дробная часть если есть НЕ учитывается
        """
        self._height = height
        self._mass_m_2 = mass_m_2
        result = int(self._width * self._length * self._mass_m_2 / 1000 * self._height)
        return result

if __name__ == '__main__':
    road = Road(5000, 20)
    print(f'Для изготовления покрытия дороги нужно {road.calculate()} тонн.')
