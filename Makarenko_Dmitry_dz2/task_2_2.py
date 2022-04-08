

def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""

    my_list = []
    for x in list_in:
        if x.isdigit():
            my_list.append('"')
            my_list.append(f'{int(x):02}')
            my_list.append('"')
        else:
            for i, c in enumerate(x):
                if c.isdigit():
                    my_list.append('"')
                    x = f'{x[0]}{abs(int(x)):02}'
            my_list.append(x)
    my_list.insert(14, '"') # по другому не придумал!
    str_out = ' '.join(my_list)
    return str_out[:3] + str_out[4:6] + str_out[7:16] + str_out[17:19] + str_out[20:54] + str_out[55:58] + str_out[59:]


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)