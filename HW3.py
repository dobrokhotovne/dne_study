# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

# версия 1
def my_func(a, b):
    global res1
    global res2
    if a == 0 and b == 0:
        print('error values!!! a=0 and b=0')
        res1 = str('error')
        res2 = str('error')
    elif a != 0 and b != 0:
        res1 = a / b
        res2 = b / a
    elif a != 0 and b == 0:
        res1 = str('error')
        res2 = 0
    elif a == 0 and b != 0:
        res1 = 0
        res2 = str('error')
my_func(a=int(input('input "a": ')), b=int(input('input "b": ')))
print('a / b = ', res1)
print('b / a = ', res2)

# версия 2
def my_func(a, b):
    global res
    res = a / b
a=int(input('input "a" : '))
b=int(input('input "b" : '))
while b == 0:
    b = int(input('input "b != 0": '))
my_func(a, b)
print('result ', a, ' / ', b, ' = ', res)


# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def my_func(name, surname, born, city, email, phone):
    print('user information: Your name is', surname, name,';    You was', born, 'born;    You are from', city, ';    Contacts:   phone -', phone, ';    e-m@il -', email)

a = input('Insert your name: ')
b = input('Insert your surname:')
c = int(input('Insert your born year:'))
d = input('Insert city, there are you living: ')
e = input('Insert your e-m@il: ')
f = input('Insert your phone number: ')

my_func(born = c, surname = b, city = d, email = e, phone = f, name = a)


# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    if a >= b and b >= c:
        res = a + b
    elif a >= b and b <= c:
        res = a + c
    elif a <= b and b <= c:
        res = b + c
    print(res)

my_func(int(input('input a:')), int(input('input b:')), int(input('input c:')))


#4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

def my_func (x, y):  # вариант 1 через **
    res = x**y
    print(res)
x = float(input('input x: '))
y = int(input('input y: '))
my_func(x, y)


def my_func(x, y):    # вариант 2 через цикл
    re = x
    for i in range(1, abs(y)):
        re = re * x
    res = 1 / re
    print(x, '^', y, '=', res)


my_func(x=float(input('input x: ')), y=int(input('input y: ')))


# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.


def my_func():
    global res
    res = 0
    while True:
        print('Please, input values. If you want stop - input "stop"')
        data = input('Input data: ').split()
        for el in data:
            'if el == 'stop:
                return
            else:
                try:
                    res += float(el)
                except ValueError:
                    print(el, 'is not number, it was not summed up!!!')
        print('summa = ', res)

my_func()
print('final summa = ', res)


# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
# возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text

def int_func():
    word = input('input word: ')
    print(word.title())

int_func()

# 7. Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделённых пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def int_func():
    global data
    while True:
        print('Please, input words. If you want stop - input "stop"')
        data = input('input data: ').split()
        i = 0
        for el in data:
            if el == 'stop':
                data[i] = el.title()
                return
            else:
                data[i] = el.title()
                i += 1
        print(data)

int_func()
print(data)
print('YOU INPUT "STOP"!!! PROGRAM  ENDED!!!')