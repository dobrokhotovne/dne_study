+# 1. Поработайте с переменными, создайте несколько, выведите на экран

# print('Задание 1. Поработайте с переменными, создайте несколько, выведите на экран')
age = 12
print(age)
print(type(age))

cash = 285.76
print(cash)
print(type(cash))

name = 'Alex'
print(name)
print(type(name))

name = str(input('Please input your name: '))
age = int(input('Please input your age: '))
cash = float(input('Please input your cash value: '))

print('Your name is', name)
print('You are', age, 'years old')
print('You have $', cash, 'in your pocket')

# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс

print('Задание 2. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс')
sec_input = int(input('Input time in seconds: '))
hour = sec_input // 3600
min = sec_input % 3600 // 60
sec = sec_input % 3600 % 60

print('Your input time is:', hour, ':', min, ':', sec)

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn

print('Задание 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn')
n = str(input('Input digit: '))
nn = n + n
nnn = n + n + n

print(n)
print(nn)
print(nnn)

res = (int(n) + int(nn) + int(nnn))
print('Result', n, '+', nn, '+', nnn, '=', res)

# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции

print('Задание 4. Найдите самую большую цифру в числе')
num_start = int(input('Input digit: '))
num = num_start
max = 0
while num > 0:
    res = num % 10
    num = num // 10
    if res > max:
        max = res
print('Maximum value in', num_start, 'is', max)

# 5.Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.

print('Задание 5. Определите, с каким финансовым результатом работает фирма')
revenue = float(input('Input revenue: '))  # выручка
costs = float(input('Input costs: '))  # издержки
if revenue > costs:
    print("Cangratulations!!! Our company has profit")
else:
    print("This time we hawe loss!!! It's bad!!!")

# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчёте на одного сотрудника.

print('Задание 6. Если фирма отработала с прибылью, вычислите рентабельность выручки')
print('и определите прибыль фирмы в расчёте на одного сотрудника.')
revenue = float(input('Input revenue: '))  # выручка
costs = float(input('Input costs: '))  # издержки
if revenue > costs:
    print("Cangratulations!!! Our company has profit")
    profit = revenue - costs  # прибыль
    rent = profit / revenue
    people = int(input('Input number of employees: '))
    single_profit = profit / people
    print(
        f'Our companu have profit {profit} and number of employees {people}. Every employer has profit {single_profit}')
else:
    print("This time we hawe loss!!! It's bad!!! No one has earned anything")

# 7. (Дополнительно). Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

print(
    'Задание 7 (Дополнительно). Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.')
a = int(input('Input first day value:'))
b = int(input('Input desired final value: '))
res = 1
while a < b:
    a = a * 1.1
    res += 1
print(f'You run {b} km on day {res}')