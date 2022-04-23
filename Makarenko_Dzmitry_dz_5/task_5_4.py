import time

def get_numbers(src: list):
    '''возвращает список с теми элементами заданного списка значения которых больше предыдущего. Работает через цикл for'''
    result = []
    for i, num in enumerate(src):
        if src[i] > src[i - 1] and i != 0:
            result.append(num)
    return result


def get_numbers_adv(src: list):
    '''возвращает список с теми элементами заданного списка значения которых больше предыдущего. Работает через list compprehensions'''
    result = [num for i, num in enumerate(src) if src[i] > src[i - 1] and i != 0]
    return result


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
start = time.perf_counter()
print(*get_numbers(src))
finish = time.perf_counter()
print(finish - start, 'for in')
start = time.perf_counter()
print(*get_numbers_adv(src))
finish = time.perf_counter()
print(finish - start, 'list compprehensions')