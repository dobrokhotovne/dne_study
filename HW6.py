# # 1. Создать класс TrafficLight (светофор).
# # определить у него один атрибут color (цвет) и метод running (запуск); атрибут реализовать как приватный;
# # в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# # продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# # переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# # проверить работу примера, создав экземпляр и вызвав описанный метод.
#
#
# from time import sleep
# class TrafficLight():
#     __color = 'Red'
#     i = 0 #счетчик итераций, выход после 5 повторов
#     def running(self):
#         while True:
#             self.__color = 'Red'
#             print(f'TrafficLight is {self.__color} now')
#             sleep(7)
#             self.__color = 'Yellow'
#             print(f'TrafficLight is {self.__color} now')
#             sleep(2)
#             self.__color = 'Green'
#             print(f'TrafficLight is {self.__color} now')
#             sleep(10)
#             self.i += 1
#             if self.i > 5:
#                 break
#
# TL1 = TrafficLight().running()
# print('TrafficLine stops')
#
# # 2 версия выполнения через список, с добавлением еще одной желтой фазы светофора при переключении с зеленого на красный
# from time import sleep
# class TrafficLight():
#     __color = ['Red', 'Yellow', 'Green']
#
#     def running(self):
#         self.i = 0
#         while True:
#             if self.i % 4 == 0:
#                 print(f'TrafficLight is {self.__color[0]} now')
#                 sleep(7)
#             elif self.i % 4 == 1:
#                 print(f'TrafficLight is {self.__color[1]} now')
#                 sleep(2)
#             elif self.i % 4 == 2:
#                 print(f'TrafficLight is {self.__color[2]} now')
#                 sleep(10)
#             else:
#                 print(f'TrafficLight is {self.__color[1]} now')
#                 sleep(2)
#             self.i += 1
#             if self.i > 10:
#                 break
#
# TL1 = TrafficLight().running()
# print('TrafficLine stops')

# 2. Реализовать класс Road (дорога). определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

# class road():
#
#     def __init__(self, length = 100, width = 20):
#         try:
#             self._lenght = length
#             self._width = width
#         except ValueError:
#             print('Input wrong values!!! Please try again')
#
#     def mass(self, length, width, thin):
#         try:
#             self._lenght = length
#             self._width = width
#             self._thin = thin
#             self._roadmass = float(self._lenght) * float(self._width) * float(self._thin) * 25
#             return f'mass of road {self._lenght} metr lenth and {self._width} metr width and {self._thin} sm thin = {self._roadmass} kilo'
#         except ValueError:
#             print('Input wrong values!!! Please try again')
#
# street1 = road()
# print(street1.mass(input('input length: '), input('input width: '), input('input thin: ')))

# # 3. Реализовать базовый класс Worker (работник).
# # определить атрибуты: name, surname, position (должность), income (доход);
# # последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# # создать класс Position (должность) на базе класса Worker;
# # в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# # проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
#
# class Worker():
#     try:
#         def __init__(self, name, surname, position, income):
#             self.name = name
#             self.surname = surname
#             self.position = position
#             self._income = income
#
#     except ValueError:
#         print('Input wrong values!!! Please try again')
#
# class Position(Worker):
#     def __init__(self, name, surname, position, income):
#         Worker.__init__(self, name, surname, position, income)
#
#     def get_full_name(self):
#         print(f'full name: {self.surname} {self.name}')
#
#     def get_total_income(self):
#         self.total_income = self._income['wage'] + self._income['bonus']
#         print(f'Total income = {self.total_income}')
#
#
# che1 = Position('Clay', 'Morrow', 'President', {"wage": 100000, "bonus": 30000})
# che1.get_full_name()
# che1.get_total_income()
# print('name - ', che1.name)
# print('surname - ', che1.surname)
# print('position - ', che1.position)
# print('income - ', che1._income)
# print('*'*50)
#
# che2 = Position('Jakson', 'Teller', 'Vice President', {"wage": 80000, "bonus": 20000})
# che2.get_full_name()
# che2.get_total_income()
# print('name - ', che2.name)
# print('surname - ', che2.surname)
# print('position - ', che2.position)
# print('income - ', che2._income)
# print('*'*50)
#
# che3 = Position('Axel', 'Lucky', 'Treasurer', {"wage": 60000, "bonus": 10000})
# che3.get_full_name()
# che3.get_total_income()
# print('name - ', che3.name)
# print('surname - ', che3.surname)
# print('position - ', che3.position)
# print('income - ', che3._income)
# print('*'*50)

# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# class Car():
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def title(self):
#         print(self.color, self.name)
#
#     def go(self):
#         print('Car start')
#
#     def stop(self):
#         print('Car stops')
#
#     def turnleft(self):
#         print('Car turn left')
#
#     def turnright(self):
#         print('Car turn right')
#
#     def showspeed(self):
#         print(f'speed = {self.speed}')
#
# class TownCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         Car.__init__(self, speed, color, name, is_police)
#
#     def showspeed(self):
#         print(f'speed = {self.speed}')
#         if self.speed > 60:
#             print('SPEED LIMIT IS 60 KM PER HOUR!!!')
#             print(f'you have exceeded the speed limit for {self.speed - 60}')
#
#
# class SportCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         Car.__init__(self, speed, color, name, is_police)
#
# class WorkCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         Car.__init__(self, speed, color, name, is_police)
#
#     def showspeed(self):
#         print(f'speed = {self.speed}')
#         if self.speed > 40:
#             print('SPEED LIMIT IS 40 KM PER HOUR!!!')
#             print(f'you have exceeded the speed limit for {self.speed - 40}')
#
# class PoliceCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         Car.__init__(self, speed, color, name, is_police)
#
# li = []
# TownCar1 = TownCar(110, 'white', 'Renault', False)
# TownCar2 = TownCar(59, 'black', 'Peugeot', False)
# WorkCar1 = WorkCar(82, 'yellow', 'VOLVO', False)
# WorkCar2 = WorkCar(38, 'orange', 'KAMAZ', False)
# SportCar1 = SportCar(240, 'red', 'Ferrari', False)
# SportCar2 = SportCar(220, 'blue', 'Lamborgini', False)
# PoliceCar1 = PoliceCar(180, 'black-white', 'Dodge', True)
# PoliceCar2 = PoliceCar(160, 'black-white', 'Dodge', True)
# li.append(TownCar1)
# li.append(TownCar2)
# li.append(WorkCar1)
# li.append(WorkCar2)
# li.append(SportCar1)
# li.append(SportCar2)
# li.append(PoliceCar1)
# li.append(PoliceCar2)
#
# for el in li:
#     el.title()
#     el.go()
#     el.turnleft()
#     el.turnright()
#     el.showspeed()
#     el.stop()
#     print('*' * 50)

# # 5. Реализовать класс Stationery (канцелярская принадлежность).
# # определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# # создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# # в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# # создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
#
# class Stationery:
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         print('Draw stars!')
#
# class Pen(Stationery):
#     def __init__(self, title):
#         Stationery.__init__(self, title)
#
#     def draw(self):
#         print(f'{self.title} draw stars!')
#
# class Pencil(Stationery):
#     def __init__(self, title):
#         Stationery.__init__(self, title)
#
#     def draw(self):
#         print(f'{self.title} draw stars!')
#
# class Handle(Stationery):
#     def __init__(self, title):
#         Stationery.__init__(self, title)
#
#     def draw(self):
#         print(f'{self.title} draw stars!')
#
# marker = Stationery('Marker')
# pen1 = Pen('Blue Pen')
# pen2 = Pen('Back Pen')
# pencil1 = Pencil('Graphit pencil')
# pencil2 = Pencil('Red pencil')
# handle1 = Handle('Orange handle')
# handle2 = Handle('Green handle')
#
# marker.draw()
# pen1.draw()
# pen2.draw()
# pencil1.draw()
# pencil2.draw()
# handle1.draw()
# handle2.draw()