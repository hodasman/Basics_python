"""
Реализовать класс Matrix (матрица).

Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков)
для формирования матрицы. В случае если список списков некорректный - возбуждать исключение ValueError с
сообщением fail initialization matrix.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде (как показано выше).
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
"""

from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        try:
            for list in matrix:
                if len(list) == len(matrix[0]):
                    continue
                else:
                    raise ValueError('ValueError:')
        except (ValueError, TypeError) as e:
            print(f'{e} fail initialization matrix')
        else:
            self.matrix = matrix

    def __str__(self):
        for list in self.matrix:
            print(f'| {" ".join(map(str,list))} |')
        return f''

    def __add__(self, other):
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))])




if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)

    print(first_matrix + second_matrix)

    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])

    fail_matrix2 = Matrix([1, 4, 9, 0, 6])