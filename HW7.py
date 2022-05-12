# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.


import sys

class Matrix:
    def __init__(self):
        try:
            self.lenth = int(input('input matrix lenth: '))
            self.height = int(input('input matrix height: '))
            ls = []
            for j in range(0, self.height):
                ls_new = []
                for i in range(0, self.lenth):
                    new = int(input(f'input element {j+1} - {i+1}: '))
                    ls_new.append(new)
                    i += 1
                ls.append(ls_new)
                j += 1
            self.ls = ls
        except ValueError:
            print('ERROR!!! Input wrong value!!! PLEASE START AGAIN!!!')
            sys.exit()

    def __str__(self): # написал сам, не смог выстроить ровно...
        self.new = ""
        for self.el in self.ls:
            self.a = ' '.join(map(str, self.el))
            self.new = self.new + (self.a) + "\n"
        return f'matrix =\n{self.new}\n***************************************'

    # второй париант метода str, нашел вывод в интернете
    # def __str__(self):
    #     for self.row in self.ls:
    #         for self.x in self.row:
    #             print(f"{self.x:6}", end="  ")
    #         print()
    #     return ''

    def __add__(self, other):
        try:
            self.ls_new = []
            self.ls_summa = []
            if self.height != other.height or self.lenth != other.lenth:
                print("ERROR!!! size matrix a != size matrix b")
                sys.exit()
            for j in range(0, self.height):
                self.ls_new = []
                for i in range(0, self.lenth):
                    self.new_el = self.ls[j][i] + other.ls[j][i]
                    self.ls_new.append(self.new_el)
                    i += 1
                self.ls_summa.append(self.ls_new)
                j += 1
            self.new = ""
            for self.el in self.ls_summa:
                self.a = ' '.join(map(str, self.el))
                self.new = (self.new + (self.a)) + "\n"
            return f'matrix a + matrix b = \n{self.new}'
        except ValueError:
            pass

a = Matrix()
b = Matrix()
print(a)
print(b)
print(a+b)


# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.

'''
куда, а главное зачем здесь применить @property, придумать не смог
'''

from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, brand, param):
        self.brand = brand
        self.param = param

    def __add__(self, other):
        self.fabric_summ = self.fabric + other.fabric
        return f'summa fabrik for {self.brand} and {other.brand} = {round(self.fabric_summ, 2)}'

    @abstractmethod
    def fabric_quant(self):
        pass

class Coat(Clothes):

    def __init__(self, brand, param):
        Clothes.__init__(self, brand, param)

    def fabric_quant(self):
        self.fabric = float(self.param) / 6.5 + 0.5
        return f'quantity of fabric for {self.brand} = {round(self.fabric, 2)}'

class Suit(Clothes):

    def __init__(self, brand, param):
        Clothes.__init__(self, brand, param)

    def fabric_quant(self):
        self.fabric = float(self.param) * 2 + 0.3
        return f'quantity of fabric for {self.brand} = {round(self.fabric, 2)}'

c1 = Coat('D&G', 48)
c2 = Coat('Gucci', 46)
c3 = Coat('Prada', 44)
s1 = Suit('Boss', 1.7)
s2 = Suit('BREONI', 1.64)
s3 = Suit('Calvin Clein', 1.95)

print(c1.fabric_quant())
print(c2.fabric_quant())
print(c3.fabric_quant())
print(s1.fabric_quant())
print(s2.fabric_quant())
print(s3.fabric_quant())

print(c1 + c2)
print(c1 + s2)


# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

class Cell:

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __add__(self, other):
        self.summ = self.count + other.count
        return f'Cell {self.name} + Cell {other.name} = {self.summ}'

    def __sub__(self, other):
        if self.count > other.count:
            self.diff = self.count - other.count
            return f'Cell {self.name} - Cell {other.name} = {self.diff}'
        else:
            return f'Cell {other.name} > Cell {self.name}. MISSION IMPOSSIBLE!!!!'

    def __mul__(self, other):
        self.comp = self.count * other.count
        return f'Cell {self.name} * Cell {other.name} = {self.comp}'

    def __truediv__(self, other):
        self.divi = self.count // other.count
        if self.divi > 0:
            return f'Cell {self.name} / Cell {other.name} = {self.divi}'
        else:
            return f'Cell {other.name} > Cell {self.name}. MISSION IMPOSSIBLE!!!!'

    def make_order(self, arg):
        self.arg = arg
        n = self.count // self.arg
        if n < 1:
            res = '*' *(self.count % self.arg)
            print(f' order =\n{res}')
        else:
            final = ''
            for el in range (1, n):
                new = '*' *(self.arg)
                final += f'{new}\n'
            res = '*' * (self.count % self.arg)
            final = final + res
            return f'\norder of Cell with {self.count} count and {self.arg} argument is \n{final}'


c1 = Cell('c1', 33)
c2 = Cell('c2', 5)
c3 = Cell('c3', 3)
c4 = Cell('c4', 10)

print(c1 + c2)
print(c1 - c4)
print(c3 - c2)
print(c2 * c3)
print(c4 / c3)
print(c2 / c4)

print(c1.make_order(4))