"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

class Date_Class:
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def date_to_int(cls, date):
        list = date.split('-')
        d = int(list[0])
        m = int(list[1])
        y = int(list[2])
        return d, m, y

    @staticmethod
    def validate_date(day, month, year):
        if 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 2022:
            return f'entered date is correct'
        else:
            raise ValueError ('incorrect date')

if __name__== '__main__':
    today = Date_Class('14-01-2015')
    print(Date_Class.date_to_int('14-01-2015'))
    print(today.date_to_int('12-02-2016'))
    print(Date_Class.validate_date(14, 1, 2015))
    print(today.validate_date(12, 13, 2016))
