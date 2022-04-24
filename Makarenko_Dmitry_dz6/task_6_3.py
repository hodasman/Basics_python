import sys
import json
import itertools


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    list_users = []
    with open(path_users_file, 'r', encoding='utf-8') as users:
        for line in users:
            list_users.append(line.replace(',', ' ').replace('\n', ''))

    with open(path_hobby_file, 'r', encoding='utf-8') as hobby:
        list_tmp = hobby.read().splitlines()
        list_hobby = list(map(lambda el: el.split(','), list_tmp))
    if len(list_hobby) > len(list_users):
        sys.exit(1)
    result = dict()
    for user, hobbys in itertools.zip_longest(list_users, list_hobby):
        result.setdefault(user, hobbys)
    return result # верните словарь, либо завершите исполнение программы кодом 1


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
