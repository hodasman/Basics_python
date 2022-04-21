tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']


def check_gen(tutors: list, klasses: list):
    for i in range(len(tutors)):
        if i >= len(klasses):
            yield (tutors[i], None)
        else:
            yield (tutors[i], klasses[i])


generator = check_gen(tutors, klasses)
print(type(generator)) # добавьте здесь доказательство, что создали именно генератор
for _ in range(len(tutors)):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration