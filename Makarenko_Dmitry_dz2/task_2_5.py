

from random import uniform


def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    for ind, num in enumerate(list_in):
        list_in[ind] = f'{int(num // 1)} руб. {round((num % 1) * 100):02} коп.'
    str_out = " ,".join(list_in)
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    list_in.sort()

    return list_in

print(id(my_list))
result_2 = sort_prices(my_list)
print(id(my_list))
print(result_2)


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    # пишите реализацию здесь
    list_out = sorted(list_in, reverse=True)
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    list_in.sort(reverse=True)
    list_out = list_in[0:5]
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)
