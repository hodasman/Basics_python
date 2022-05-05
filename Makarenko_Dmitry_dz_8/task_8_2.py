import re

def get_parse_attrs(line: str) ->tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>)"""
    RE_IP = re.compile(r'^(\w+[.:])+\w+')
    RE_DATE = re.compile(r'\d+/\w+/(\d+:){3}\d{2}\s+\+\d{4}')
    RE_TYPE = re.compile(r'(?<=")([A-Z]{3,4})')
    RE_SOURSE = re.compile(r'/[a-z]+/\w+')
    RE_CODE = re.compile(r'(?<=HTTP/1.1"\s)(\d+)')
    RE_SIZE = re.compile(r'(?<=HTTP/1.1"\s\d{3}\s)(\d+)')
    result_corteg = (RE_IP.search(line).group(), RE_DATE.search(line).group(), RE_TYPE.search(line).group(), RE_SOURSE.search(line).group(), RE_CODE.search(line).group(), RE_SIZE.search(line).group())
    return result_corteg


with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        print(get_parse_attrs(line))



