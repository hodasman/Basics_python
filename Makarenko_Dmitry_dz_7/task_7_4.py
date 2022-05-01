import os

def direct_scanner(folder: str) -> dict:
    '''
    Возвращает статистику для заданной папки в виде словаря в котором ключи —
    верхняя граница размера файла, а значения — общее
    количество файлов (в том числе и в подпапках), размер которых не превышает
     этой границы, но больше предыдущей.
     '''
    file_size = []
    for root, dirs, files in os.walk(folder): # Сканируем папку и добавляем значения размеров файлов в список
        for file in files:
            file_size.append(os.stat(os.path.join(root, file)).st_size)
    max_size = 0
    for size in file_size: # Определяем максимальный размер файла
        if size > max_size:
            max_size = size
    digit = len(str(max_size)) # Определяем разряд числа максимального размера файла
    max_border = [10 ** n for n in range(1, digit + 1)] # Создаем список будущих ключей словаря от 10 и до макс разряда
    min_border = [10 ** n for n in range(digit + 1)] # Создаем такой же список но первый элемент равен 0
    min_border[0] = 0
    result_dict = {}

    for max, min in zip(max_border, min_border): # Проходимся по картежам из элементов первого и второго списков
        list_temp = []
        for file in file_size:
            if min <= file <= max:
                list_temp.append(file)
        result_dict.setdefault(max, len(list_temp)) if len(list_temp) != 0 else None
    return result_dict


print(direct_scanner('/Users/Macintosh/Library/Python/3.8/lib/python/site-packages/django'))