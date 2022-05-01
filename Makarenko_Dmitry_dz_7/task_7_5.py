import json
import os
from pprint import pprint

def direct_scanner_adv(folder: str) -> dict:
    '''
    Возвращает статистику для заданной папки в виде словаря в котором ключи —
    верхняя граница размера файла, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]),
    где <files_quantity> - количество файлов (в том числе и в подпапках), размер которых не превышает
     этой границы, но больше предыдущей, а [<files_extensions_list>] - список из типов расширений этих файлов.
     '''
    try:
        size_ext = []
        for root, dirs, files in os.walk(folder): # Сканируем папку и создаем список состоящий из кортежей вида (размер файла, расширение файла)
            for file in files:
                size_ext.append((os.stat(os.path.join(root, file)).st_size, file.rsplit('.', maxsplit=1)[-1].lower()))
    except EOFError as e:
        print(f'Error: {e}')
    max_size = 0
    for size, ext in size_ext: # Определяем максимальный размер файла в списке кортежей
        if size > max_size:
            max_size = size
    digit = len(str(max_size)) # Определяем разряд числа максимального размера файла
    max_border = [10 ** n for n in range(1, digit + 1)] # Создаем список будущих ключей словаря от 10 и до макс разряда
    min_border = [10 ** n for n in range(digit + 1)] # Создаем такой же список но первый элемент равен 0
    min_border[0] = 0
    result_dict = {}

    for max, min in zip(max_border, min_border): # Проходимся по картежам из элементов первого и второго списков
        list_size = []
        set_ext = set()
        for size, ext in size_ext:
            if min <= size <= max:
                list_size.append(size) # Размеры файла подходящие под условия будем добавлять в временный список
                set_ext.add(ext)  # Расширения файлов будем добавлять в множество, чтобы избежать повторений
        result_dict.setdefault(max, (len(list_size), list(set_ext))) if len(list_size) != 0 else None
    return result_dict


statistics_dir = direct_scanner_adv('/Users/Macintosh/Library/Python/3.8/lib/python/site-packages/urllib3')
pprint(statistics_dir)
with open(os.path.join(os.getcwd(), 'urllib3_summary.json'), 'w', encoding='utf-8') as f:
    json.dump(statistics_dir, f)