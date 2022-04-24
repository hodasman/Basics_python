import sys
import json
import itertools


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> list:
    """
    Считывает данные из файлов и возвращает список с объединенными данными из двух списков
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: List(str: str|None])
    """
    list_users = []
    with open(path_users_file, 'r', encoding='utf-8') as users:
        for line in users:
            list_users.append(line.replace('\n', ': '))
    list_hobby = []
    with open(path_hobby_file, 'r', encoding='utf-8') as hobby:
        for line in hobby:
            list_hobby.append(line)
    if len(list_hobby) > len(list_users):
        sys.exit(1)
    result = []
    for user, hobbys in itertools.zip_longest(list_users, list_hobby):
        result.append(f'{user}{hobbys}')
    return result # верните список, либо завершите исполнение программы кодом 1


list_out = prepare_dataset('users.csv', 'hobby.csv')
print(list_out)
with open('users_hobby.txt', 'x', encoding='utf-8') as f:
    f.writelines(list_out)
