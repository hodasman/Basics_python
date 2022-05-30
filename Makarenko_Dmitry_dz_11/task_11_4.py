"""
Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. А также
класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведённых типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за
приём оргтехники на склад и передачу в определённое подразделение компании. Для
хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру (например, словарь)

Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
"""



class Warehouse:
    def __init__(self):
        self.printers: set = set()
        self.scaners: set = set()
        self.xerox: set = set()
        self.other: set = set()
        self.title = 'office equipment'
        self.count = 0

    def __setattr__(self, key, value):
        if key == 'title' and isinstance(value, str):
            self.__dict__[key] = value
        elif key == 'printers':
            self.__dict__[key] = value
        elif key == 'scaners':
            self.__dict__[key] = value
        elif key == 'xerox':
            self.__dict__[key] = value
        elif key == 'other':
            self.__dict__[key] = value
        elif key == 'count':
            self.__dict__[key] = value
        else:
            print(f'Атрибут {key} или значение {value} не допустимы')

    def load(self, *args):
        """Загрузка техники на склад"""
        count = 0
        for box in args:
            if isinstance(box, Printers):
                self.printers.add(box)
                count += 1
            elif isinstance(box, Scaners):
                self.scaners.add(box)
                count += 1
            elif isinstance(box, Xerox):
                self.xerox.add(box)
                count += 1
            else:
                self.other.add(box)
                count += 1
        self.count += count
        print(f'На склад поступило {count} единиц техники.')

    def upload(self, *args, subdivision: set):
        """Выгрузка из склада"""
        count = 0
        for box in args:
            if isinstance(box, Printers):
                self.printers.remove(box)
                subdivision.add(box)
                count += 1
            elif isinstance(box, Scaners):
                self.scaners.remove(box)
                subdivision.add(box)
                count += 1
            elif isinstance(box, Xerox):
                self.xerox.remove(box)
                subdivision.add(box)
                count += 1
            else:
                self.other.remove(box)
                subdivision.add(box)
                count += 1
        self.count -= count
        print(
            f'Со склада выгружено {count} единиц техники.')

    def __str__(self):
        return f'Склад {self.title}\n Всего техники: {self.count}\n Принтеров: {len(self.printers)}\n' \
               f' Сканеров: {len(self.scaners)}\n Ксероксов: {len(self.xerox)}\n Другой техники: {len(self.other)}'


class OfficeEquipment:
    def __init__(self, brand: str, cost: float, stock: set):
        self.brand = brand
        self.cost = cost
        self.used = False
        self.stock = stock
        self.stock.add(self)

    def __setattr__(self, key, value):
        if key == 'brand' and isinstance(value, str):
            self.__dict__[key] = value
        elif key == 'brand' and not isinstance(value, str):
            print(f'Не верное значение {key} для объекта {self.__class__.__name__}, ожидаемое значение str')
        elif key == 'cost' and isinstance(value, float):
            self.__dict__[key] = value
        elif key == 'cost' and not isinstance(value, float):
            print(f'Не верное значение {key} для объекта {self.__class__.__name__}, ожидаемое значение float')
        elif key == 'used' and isinstance(value, bool):
            self.__dict__[key] = value
        elif key == 'stock' and isinstance(value, set):
            self.__dict__[key] = value
        elif key == 'stock' and not isinstance(value, set):
            print(f'Не верное значение {key} для объекта {self.__class__.__name__}, ожидаемое значение set')

    def __add__(self, other):
        print(f'Общая стоимость {self.cost + other.cost}')


class Printers (OfficeEquipment):
    def __init__(self, brand: str, cost: float, technology: str, stock: set):
        super().__init__(brand, cost, stock)
        self.technology = technology

    def __setattr__(self, key, value):
        OfficeEquipment.__setattr__(self, key, value)
        if key == 'technology' and isinstance(value, str):
            self.__dict__[key] = value
        elif key == 'technology' and not isinstance(value, str):
            print(f'Не верное значение {key} для объекта {self.__class__.__name__}, ожидаемое значение str')

    def __str__(self):
        try:
            return f'Принтер {self.brand} {self.technology} стоимость: {self.cost}$ Состояние: ' \
                   f'({"б/у" if self.used else "новый"})'
        except AttributeError as e:
            return f'Error! {e}'


class Scaners (OfficeEquipment):
    def __init__(self, brand: str, cost: float, dpi: int, stock: set):
        super().__init__(brand, cost, stock)
        self.dpi = dpi

    def __setattr__(self, key, value):
        OfficeEquipment.__setattr__(self, key, value)
        if key == 'dpi' and isinstance(value, int):
            self.__dict__[key] = value
        elif key == 'dpi' and not isinstance(value, int):
            print(f'Не верное значение {key} для объекта {self.__class__.__name__}, ожидаемое значение int')

    def __str__(self):
        try:
            return f'Сканер {self.brand} выходное разрешение: {self.dpi}dpi, стоимость: {self.cost}$ Состояние: ' \
                   f'{"б/у" if self.used else "новый"}'
        except AttributeError as e:
            return f'Error! {e}'


class Xerox(OfficeEquipment):
    def __init__(self, brand: str, cost: float, speed: int, stock: set):
        super().__init__(brand, cost, stock)
        self.speed = speed

    def __setattr__(self, key, value):
        OfficeEquipment.__setattr__(self, key, value)
        if key == 'speed' and isinstance(value, int):
            self.__dict__[key] = value
        elif key == 'speed' and not isinstance(value, int):
            print(f'Не верное значение {key} для объекта {self.__class__.__name__}, ожидаемое значение int')

    def __str__(self):
        try:
            return f'Ксерокс {self.brand} скорость печати: {self.type}стр/мин стоимость: {self.cost}$ Состояние: ' \
                   f'{"б/у" if self.used else "новый"}'
        except AttributeError as e:
            return f'Error! {e}'


if __name__ == "__main__":
    s = set()
    printer_1 = Printers('Canon', 52.50, 'лазерный', stock=s)
    printer_2 = Printers('Samsung', 30.0, 'струйный', stock=s)
    printer_1.used = True

    xerox = Xerox('HP', 120.90, 20, stock=s)

    scaner_1 = Scaners('Lexmark', 44, 1000, stock=s)
    scaner_2 = Scaners('HP', 60.0, 1500, stock=s)
    print(scaner_1)

    w = Warehouse()
    w.load(*s)
    print(w)
    buhgalter = set()
    w.upload(printer_2, scaner_2, subdivision=buhgalter)
    print(w)
