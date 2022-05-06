# 1. Создать программный файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

file = open(r'dne_lesson5_1.txt', 'w', encoding='utf-8')
while True:
    new = input('input new line:')
    if new == '':
        break
    file.write(f'{new}\n')
file.close()


# 2. Создать текстовый файл (не программно),
# сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open(r'dne_lesson5_2.txt', "r", encoding='utf-8') as file:
    ls = file.readlines()
    print(ls)
    print('lines count = ',len(ls))
    j = 1
    for i in ls:
        print(f'{j} line has {len(i)} symbols')
        j += 1


# 3. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

with open(r'dne_lesson5_3.txt', "r", encoding='utf-8') as file:
     ls = file.readlines()
     new = 0
     print(ls)
     for i in ls:
         j = i.split()
         new = new + float(j[1])
         if float(j[1]) < 20000.00:
             print(f'{j[0]} has salary less 20000')
     aver = round(new, 2) / len(ls)
     print(f'average value = {round(aver, 2)}')


# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

di = {'One' : 'Один',  'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
with open(r'dne_lesson5_4.txt', "r", encoding='utf-8') as file:
    ls = file.readlines()
    with open(r'dne_lesson5_4_2.txt', "w", encoding='utf-8') as file:
        for line in ls:
            el = line.split()
            el[0] = di[el[0]]
            file.write(' '.join(el))
            file.write(f'\n')


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

import random
with open(r'dne_lesson5_5.txt', "w", encoding='utf-8') as file:
    while True:
        n = int(random.random() * 1000 // 30)
        if n > 0:
            break
    print('random quantity of elements = ', n)
    for i in range(0, n):
        file.write(f'{str(round((random.random() * 1000), 2))}  ')

with open(r'dne_lesson5_5.txt', "r", encoding='utf-8') as file:
    ls = file.readline().split()
    sum = 0
    for i in ls:
        sum = sum + float(i)
    print('The amount of elements = ',  round(sum, 2))


# 6. Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.

with open(r'dne_lesson5_6.txt', "r", encoding='utf-8') as file:
    ls = file.readlines()
    n = len(ls)
    di = {}
    sum = 0
    for el in ls:
        el_new = el.split()
        for i in range(1, len(el_new)):
            while True:
                if el_new[i].isdigit() == True:
                    sum = sum + int(el_new[i])
                    break
                elif el_new[i] == '-':
                    break
                else:
                    el_new[i] = el_new[i][:-1]
            di[el_new[0]] = sum
        sum = 0
    print(di)


# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).

import json
with open(r'dne_lesson5_7.txt', "r", encoding='utf-8') as file:
    ls = file.readlines()
    n = len(ls)
    di_firm = {}
    di_av = {}
    sum = 0
    i = 0
    for el in ls:
        el_new = el.split()
        if int(el_new[2]) > int(el_new[3]):
            profit = int(el_new[2]) - int(el_new[3])
            i +=1
            sum = sum + profit
            di_firm[el_new[0]] = profit
    aver = sum / i
    di_av['average_profit'] = aver
    lis = [di_firm, di_av]
    js = json.dumps(lis)
    print(js)
    with open(r'dne_lesson5_7.json', "w", encoding='utf-8') as file:
        json.dump(lis, file)