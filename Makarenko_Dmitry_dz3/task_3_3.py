

def thesaurus(*args) -> dict:
    """Возвращает словарь в котором ключи - это первые буквы имен, а значения - списки имен, начинающиеся с этих букв"""
    list_1 = []
    dict_1 = {}
    for arg in args:
        list_1.append(arg[0])
    for letter in list_1:
        dict_1.setdefault(letter, list(filter(lambda el: el.startswith(letter), args)))
    return dict_1


print(thesaurus('Мария', 'Иван', 'Дмитрий', 'Елена', 'Екатерина', 'Денис'))