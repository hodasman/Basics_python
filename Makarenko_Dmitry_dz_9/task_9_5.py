"""
Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:

    def __init__(self, title: str) -> None:
        self.title = title

    def draw(self) -> None:
        print('Запуск отрисовки')


# определите классы ниже согласно условий задания
class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self) -> None:
        print(f'{__class__.__name__}: приступил к отрисовке объекта "{self.title}"')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self) -> None:
        print('Запуск отрисовки')
        print(f'{__class__.__name__}: приступил к отрисовке объекта "{self.title}"')
class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self) -> None:
        print(f'{__class__.__name__}: приступил к отрисовке объекта "{self.title}"')


if __name__ == '__main__':
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')
    pen.draw()  # Pen: приступил к отрисовке объекта "Ручка"
    handle.draw()  # Handle: приступил к отрисовке объекта "Маркер"
    pencil.draw()  # Пример вывода ниже в многострочном комментарии
    """
    Запуск отрисовки
    Pencil: приступил к отрисовке объекта "Карандаш"
    """