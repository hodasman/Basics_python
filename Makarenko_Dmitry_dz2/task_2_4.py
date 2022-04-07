
def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    list_out = []
    for s in my_list:
        x = s.split()
        list_out.append(f' Привет, {x[-1].capitalize()}! ')
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)