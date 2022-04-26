from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    list_1 = line.split()
    corteg = (list_1[0], list_1[5][1:], list_1[6])
    return  corteg # верните кортеж значений <remote_addr>, <request_type>, <requested_resource>


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        list_out.append(get_parse_attrs(line)) # передавайте данные в функцию и наполняйте список list_out кортежами

pprint(list_out)

