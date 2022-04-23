import time

def get_uniq_numbers(src: list):
    '''Возвращает список из уникальных элементов начального списка'''
    result = []
    for el in src:
        if src.count(el) == 1:
            result.append(el)
    return result


def get_uniq_numbers_adv(src: list):
    '''Возвращает список из уникальных элементов начального списка'''
    unical = set()
    tmp = set()
    for el in src:
        if el not in tmp:
            unical.add(el)
        else:
            unical.discard(el)
        tmp.add(el)
    result = [el for el in src if el in unical]
    return result

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 10, 7, 4, 11]
start = time.perf_counter()
print(*get_uniq_numbers(src))
finish = time.perf_counter()
print(finish - start, '1 вариант')
start = time.perf_counter()
print(*get_uniq_numbers_adv(src))
finish = time.perf_counter()
print(finish - start, '2 вариант')