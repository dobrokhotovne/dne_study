# 1. 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

name = 'Max'
age = 36
man = True
cash = 5684.12
city = 'Moscow'
ls = [name, age, man, cash, city]
print((ls[0]))
print(type(ls[0]))
print((ls[1]))
print(type(ls[1]))
print((ls[2]))
print(type(ls[2]))
print((ls[3]))
print(type(ls[3]))
print((ls[4]))
print(type(ls[4]))


# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

n = int(input('Input number of elements: ')) # ввод количества элементов списка
ls = []
for i in range(n):  # ввод элеметов списка
    print('Input ',i+1 ,' element: ')
    el = input()
    ls.append(el)
print(ls)

n = n//2 # Поиск необходимого количества замен элементов
j = 0 # Доп переменная
for i in range(n):
    ls[j], ls[j+1] = ls[j+1], ls[j]
    j+=2
print(ls)


# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

n = int(input('Input month number : '))
while n > 12 or n < 1:
    print('wrong value')
    n = int(input('Input month number : '))

# Решение через list
ls = ['WINTER', 'SPRING', 'SUMMER', 'AUTUMN']
if n <= 2 or n == 12:
    print('result from list: ', ls[0])
elif n < 6:
    print('result from list: ', ls[1])
elif n < 9:
    print('result from list: ', ls[2])
elif n < 12:
    print('result from list: ', ls[3])
print('_' *30)
# Решение через dict
di = {'winter' : [1, 2, 12], 'spring' : [3, 4, 5], 'summer' : [6, 7, 8],'autumn' : [9, 10, 11]}
for el in di:
    if n in di[el]:
        print('result from dict: ', el)


# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

line = input ("Input line: ").split()
for i in range(len(line)):
        print(i+1, '. ',line[i][:10])



# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [68, 54, 42, 22, 18, 10, 8, 5]
print(my_list)
new = int(input('Input new value: '))
for i in range(len(my_list)):
    if new > my_list[i]:
        my_list.insert(i, new)
        break
    elif new == my_list[i]:
        my_list.insert(i+1, new)
        break
    elif new < my_list[len(my_list)-1]:
        my_list.insert(len(my_list), new)
        break
print(my_list)



# 6. (Дополнительно) Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.

prod = 'product'
price = 'price'
count = 'count'
unit = 'unit'
di = {prod : [], price : [], count : [], unit : []}
cort1 = (1, {prod : 'PC', price : 200000, count: 15, unit : 'psc.' })
cort2 = (2, {prod : 'PlayStatison', price : 60000, count: 3, unit : 'psc.' })
cort3 = (3, {prod : 'X-Box', price : 50000, count: 7, unit : 'psc.'})
cort4 = (4, {prod : 'Nintendo VII', price : 40000, count: 10, unit : 'psc.'})
cort5 = (5, {prod : 'Sega', price : 3000, count: 62, unit : 'psc.'})
cort6 = (6, {prod : 'Dandy', price : 600, count: 12, unit : 'psc.'})
print(cort1)
print(cort2)
print(cort3)
print(cort4)

for i in di:
 di[i].append(cort1[1][i]), di[i].append(cort2[1][i]), di[i].append(cort3[1][i]), di[i].append(cort4[1][i]), di[i].append(cort5[1][i]), di[i].append(cort6[1][i])
 di[i] = list(set(di[i])) #удаление повторяющихся элементов

print(di)