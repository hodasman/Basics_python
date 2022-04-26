
def get_most_frequent(list_in: list):
    """Возвращает элемент списка, который встречается чаще других"""
    list_set = set(list_in)
    most_frequent = None
    max_count = 0
    for item in list_set:
        temp = list_in.count(item)
        if temp > max_count:
            max_count = temp
            most_frequent = item
    return most_frequent


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        list_out.append(line.split()[0])

print(get_most_frequent(list_out))

