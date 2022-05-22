"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class DivisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt
try:
    divident = int(input('Введите делимое число: '))
    divider = int(input('Введите делитель: '))

    if divider == 0:
        raise DivisionByZero('Делитель не может быть нулем')
except ValueError:
    print('Вы ввели не число')
except DivisionByZero as err:
    print(err)
else:
    print(divident / divider)