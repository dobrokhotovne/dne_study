# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date():

    def __init__(self, value):
        self.value = value

    @classmethod
    def date_int(cls, value):
        cls.value = value
        ls = cls.value.split('-')
        print(f'{ls[0]} {ls[1]} {ls[2]}')


    @staticmethod
    def date_valid(value):
        value = value
        try:
            ls = value.split('-')
            if int(ls[0]) > 31 or int(ls[0]) < 1:
                print('input wrong day value!!!')
            elif int(ls[1]) > 12 or int(ls[1]) < 1:
                print('input wrong month value!!!')
            elif int(ls[2]) < 1:
                print('input wrong year value!!!')
            elif int(ls[1]) == 2 and int(ls[0]) > 28:
                print('input wrong day value in february!!!')
            else:
                print(f'{ls[0]} {ls[1]} {ls[2]}')
        except ValueError:
            print('ERROR!!! Wrong type of inputed value!')


Date.date_int('35-12-2020')
Date.date_int('20-0-1996')
Date.date_int('20-12-0')
Date.date_int('30-02-2021')
Date.date_int('20-08-2022')
Date.date_int('22-04-1989')

Date.date_valid('35-12-2020')
Date.date_valid('20-0-1996')
Date.date_valid('20-12-0')
Date.date_valid('30-02-2021')
Date.date_valid('20-08-2022')
Date.date_valid('22-04-1989')

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyError(Exception):

    def __init__(self, text):
        self.text = text

a = input('Input divisible: ')
b = input('Input divider != 0: ')

try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise MyError('ERROR!!! Divider = 0!!!')
    else:
        c = a / b
        print(f'divisible / divider = {c}')
except ValueError:
    print('ERROR!!! Wrong type of inputed value!')
except MyError as mr:
    print(mr)


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду «stop».
# При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
# Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

from sys import exit

class MyError(Exception):

    def __init__(self, text):
        self.text = text

ls = []
while True:
    try:
        a = input('input a string of numbers, separated by a space. If you want stop - input stop: ')
        a = a.split(' ')
        for el in a:
            if el.lower() == 'stop':
                print(f'You stop programm! result = {ls}')
                exit()
            elif el.isdigit() != True:
                raise MyError(f'!!!ERROR!!! Wrong type of inputed value! Last result: \n {ls}')
            else:
                ls.append(el)
    except MyError as mr:
        print(mr)

print(ls)


# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Warehouse:

    def __init__(self, name):
        self.name = name
        self.dict = {}

    def arrive(self, equipment):
        self.dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        if self.dict[name]:
            self.dict.setdefault(name).pop(0)

    def count(self):
        n = len(self.dict['Scan']) + len(self.dict['Print']) + len(self.dict['Copy'])
        print(f' in Warehouse {self.name} is {n} Equipments')

class Equipment():

    def __init__(self, name, speed, year):
        self.name = name
        self.speed = speed
        self.year = year
        self.group = self.__class__.__name__

    @property
    def year(self):
        return self.__y

    @year.setter
    def year(self, year):
        if year < 1996:
            self.__y = 1996
        elif year > 2022:
            self.__y = 2022
        else:
            self.__y = year

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.speed} {self.__y}'


class Print(Equipment):

    def __init__(self, series, name, speed, year):
        super().__init__(name, speed, year)
        self.series = series
        self.__y = year

    def __repr__(self):
        return f'{self.name} {self.series} {self.speed} {self.year}'

    def action(self):
        return 'Печатает'


class Scan(Equipment):

    def __init__(self, name, speed, year):
        super().__init__(name, speed, year)

    def action(self):
        return 'Сканирует'


class Copy(Equipment):

    def __init__(self, name, speed, year, duplex):
        super().__init__(name, speed, year)
        self.duplex = duplex

    def action(self):
        return 'Копирует'

    def __repr__(self):
        return f'{self.name} {self.speed} {self.year} {self.duplex}'


WH = Warehouse('Scolkovo')
s1 = Scan('hp', 20, 1995)
print(s1)
WH.arrive(s1)
s2 = Scan('Epson', 16, 2021)
WH.arrive(s2)
s3 = Scan('Kyocera', 33, 2032)
WH.arrive(s3)
p1 = Print('21x', 'Sony', 25, 2018)
WH.arrive(p1)
c1 = Copy('XEROX', 33, 2022, True)
WH.arrive(c1)
print(WH.dict)
WH.count()
WH.extract('Scan')
print(WH.dict)
WH.count()
WH.extract('Scan')
print(WH.dict)
WH.count()
WH.extract('Scan')
print(WH.dict)
WH.count()

# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        return f'The sum is equal to {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Еhe product is equal to {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'Complex number = {self.a} + {self.b} * i'


c1 = Complex(1, -2)
c2 = Complex(2, 3)
print(c1)
print(c1 + c2)
print(c1 * c2)