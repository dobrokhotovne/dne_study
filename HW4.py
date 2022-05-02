# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

path, hour, price, extra = argv
try:
    wages = float(hour) * float(price) + float(extra)
    print('for', hour, 'workhours with price $', price, ' per hour and prize ', extra, 'you got $', wages)
except ValueError:
    print('Input wrong values!!! Try again')


# 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

ls = (input('input numbers: ').split())
try:
    ls_new = [ls[i] for i in range(0, len(ls)) if int(ls[i]) > int(ls[i-1])]
    print(ls_new)
except ValueError:
    print('Input wrong values!!! Please try again')

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Решите задание в одну строку.

ls = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0 ]
print(ls)

# 4. Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию.
# Элементы выведите в порядке их следования в исходном списке.
# Для выполнения задания обязательно используйте генератор.

ls = (input('input numbers list: ').split())
try:
    ls_new = [el for el in ls if ls.count(el) == 1]
    print(ls_new)
except ValueError:
    print('Input wrong values!!! Please try again')

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.

from functools import reduce

ls = [i for i in range(100, 1001, 2)]
print(ls)
res = reduce(lambda x, y: x * y, ls)
print(res)


# 6. Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;

#печатает 10 значений после указанного
n = int(input('input start value:'))
new = [el for el in range(n , n + 10)]
print(new)

# печатает заданный пользователем диапазон
new = [el for el in range(int(input('input start value:')), int(input('input last value:')) + 1)]
print(new)

# через count:
from itertools import count

i = 0
try:
    for el in count (int(input('input start value: '))):
        print (el)
        i += 1
        if i > 15:
            break
except ValueError:
    print('Input wrong values!!! Please try again')

#  итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения.

from itertools import cycle

i = 0
for el in cycle(input('input words: ')):
    print(el)
    i += 1
    if i > 30:
        break

#7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
from math import factorial

def fact(n):
    new = (el for el in range (1, n + 1))
    for el in new:
        el = factorial(el)
        yield el

g = fact(int(input('input last value:')) + 1)
for el in g:
    print(el)