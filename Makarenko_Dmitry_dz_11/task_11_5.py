"""
Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное
число». Реализовать перегрузку методов сложения и умножения комплексных чисел.
Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа),
выполнить сложение и умножение созданных экземпляров. Проверить корректность
полученного результата.
"""


class ComplexNumber:

    def __init__(self, a: float, b: float):
        self.a = a  # действительное число
        self.b = b  # мнимое число

    def __str__(self):
        return f'{self.a}{"+" if self.b >= 0 else ""}{self.b}i'

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)


if __name__ == "__main__":
    g = ComplexNumber(1, -1)
    f = ComplexNumber(3, 6)
    print(g + f)
    print(g * f)
