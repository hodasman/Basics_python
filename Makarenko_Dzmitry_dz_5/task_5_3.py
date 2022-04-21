tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]

def generator():
    for i in range(len(tutors)):
        if i >= len(klasses):
            yield (tutors[i], None)
        else:
            yield (tutors[i], klasses[i])
print(type(generator()))
print(*generator(), sep='')