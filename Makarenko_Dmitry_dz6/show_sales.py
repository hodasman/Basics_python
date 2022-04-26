import sys

with open('bakery.csv', 'r') as f:
    list_1 = f.readlines()
if len(sys.argv) == 1:
    for el in list_1:
        print(el.replace('\r\n', ''))
elif len(sys.argv) == 2:
    if int(sys.argv[1]) > len(list_1):
        print(None)
    list_2 = list_1[int(sys.argv[1]) - 1:]
    for el in list_2:
        print(el.replace('\r\n', ''))
else:
    if int(sys.argv[1]) > int(sys.argv[2]):
        print(None)
    list_3 = list_1[int(sys.argv[1]) - 1:int(sys.argv[2])]
    for el in list_3:
        print(el.replace('\r\n', ''))

