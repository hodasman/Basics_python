def num_translate(num: str) -> str:
    num_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    str_out = num_dict.get(num)
    return str_out


print(num_translate('fifty'))