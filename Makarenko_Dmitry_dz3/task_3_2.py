def num_translate_adv(num: str) -> str:
    """переводит числительные от 0 до 10 c английского на русский язык"""
    num_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if num.istitle():
        str_out = num_dict.get(num.lower())
        return str_out.capitalize()
    else:
        str_out = num_dict.get(num)
        return str_out



print(num_translate_adv('Ten'))