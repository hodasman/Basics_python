def thesaurus(*args) -> dict:
    """Возвращает словарь в котором ключи - это первые буквы имен, а значения - списки имен, начинающиеся с этих букв"""
    list_let = []
    dict_out = {}
    for arg in args:
        list_let.append(arg[0])
        list_let.sort()
    for letter in list_let:
        dict_out.setdefault(letter, list(filter(lambda el: el.startswith(letter), args)))
    return dict_out

def thesaurus_adv(*args) -> dict:
    """Возвращает словарь, в котором ключи — первые буквы фамилий, а значения — словари"""
    list_2 = []
    dict_out = {}
    def accepted(el):
        y = el.split()
        return y[1].startswith(letter)
    for arg in args:
        x = arg.split()
        list_2.append((x[1])[0])
        list_2.sort()
    for letter in list_2:
        dict_out.setdefault(letter, thesaurus(*filter(accepted, args)))

    return dict_out


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Ирина Савич", "Алина Сиднева", "Денис Артюх", "Мария Колесникова"))