def get_jokes(n: int) -> list:
    """возвращает n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)"""
    from random import choice
    list_out = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    i = 0
    while i < n:
        list_out.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        i += 1
    return list_out


print(get_jokes(5))
