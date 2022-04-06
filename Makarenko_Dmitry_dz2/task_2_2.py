
List = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
my_list = []
for x in List:
    if x.isdigit():
        my_list.append('"')
        my_list.append(f'{int(x):02}')
        my_list.append('"')
    else:
        for i, c in enumerate(x):
            if c.isdigit():
                my_list.append('"')
                x = f'{x[0]}{abs(int(x)):02}'
        my_list.append(x)
my_list.insert(14, '"')
print(' '.join(my_list))
