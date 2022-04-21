def get_jokes(n: int, repeat='yes') -> list:
    """возвращает n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого), флаг repeat позволяет или запрещает повторы слов в шутках"""
    from random import choice, randrange
    list_out = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    i = 0
    if repeat == 'yes':
        while i < n:
            list_out.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
            i += 1
        return list_out
    else:
        if n > len(nouns):
            print('Количество слов в списке меньше, чем введенное вами количество неповторяющихся шуток')
        else:
            while i < n:
                a = randrange(0, len(nouns))
                b = randrange(0, len(adverbs))
                c = randrange(0, len(adjectives))
                list_out.append(f'{nouns[a]} {adverbs[b]} {adjectives[c]}')
                del nouns[a], adverbs[b], adjectives[c]
                i += 1
            return list_out


print(get_jokes(5, 'no'))
