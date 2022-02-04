# Задание 1 

import time

class TrafficLight:
    __color1 = "красный"
    __color2 = "желтый"
    __color3 = "зеленый"
   
    def running(self):
        print(TrafficLight.__color1)
        time.sleep(7)
        print(TrafficLight.__color2)
        time.sleep(2)
        print(TrafficLight.__color3)

sign = TrafficLight()
sign.running() 

# Задание 2 

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.mass1m1cm = 25
        self.thickness = 5
        
    def mass_asph(self):
        result_mass = self._length * self._width * self.mass1m1cm * self.thickness
        result_mass = result_mass / 1000
        print(f"Необходимая масса асфальта составляет {result_mass} т")

my_length = int(input("Введите длину полотна "))
my_width = int(input("Введите ширину полотна "))
a = Road(my_length, my_width)
a.mass_asph()

    
# Задание 3

class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income
        
class Position(Worker):
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)
        
    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        print(f"Полное имя сотрудника - {full_name}")
        
    def get_total_income(self):
        total_income = sum(self._income.values())
        print(f"Зарплата сотрудника - {total_income}")
  
    
name = input("Введите имя сотрудника ")
surname = input("введите фамилию сотрудника ")
position = input("Введите должность сотрудника ")
wage = int(input("Введите оклад сотрудника "))
bonus = int(input("Введите премию сотрудника "))

_income = {"wage": wage, "bonus": bonus}  

worker_1 = Position(name, surname, position, _income)
print(f"Имя сотрудника - {worker_1.name}")
print(f"Фамилия сотрудника - {worker_1.surname}")
print(f"Должность сотрудника - {worker_1.position}")
worker_1.get_full_name()
worker_1.get_total_income()
    
         
     
# Задание 4


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        
    def go(self):
        print("Машина поехала ")
        
    def stop(self):
        print(" Машина остановилась ")
        
    def turn(self):
        print("Машина повернула направо ")
        
    def show_speed(self):
        print(f"Текущая скорость автомобиля - {self.speed} км/ч")

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    
    def show_speed(self):
        if self.speed > 60:
            print(f"Текущая скорость автомобиля - {self.speed} км/ч. Вы превысили скорость!")
        else:
            print(f"Текущая скорость автомобиля - {self.speed} км/ч")  
            
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        
    def show_speed(self):
        if self.speed > 40:
            print(f"Текущая скорость автомобиля - {self.speed} км/ч. Вы превысили скорость!")
        else:
            print(f"Текущая скорость автомобиля - {self.speed} км/ч")  

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


my_town = TownCar(70, 'black', 'honda', False)
print(f"Название автомобиля - {my_town.name}")
print(f"Скорость - {my_town.speed}")
print(f"Цвет авто - {my_town.color}")
print(f"Машина полицейская? {my_town.is_police}")
my_town.go()
my_town.stop()
my_town.turn()
my_town.show_speed()


my_sport = SportCar(90, 'white', 'ferrari', False)
print(f"Название автомобиля - {my_sport.name}")
print(f"Скорость - {my_sport.speed}")
print(f"Цвет авто - {my_sport.color}")
print(f"Машина полицейская? {my_sport.is_police}")
my_sport.go()
my_sport.stop()
my_sport.turn()
my_sport.show_speed()

my_work = WorkCar(70, 'red', 'toyota', False)
print(f"Название автомобиля - {my_work.name}")
print(f"Скорость - {my_work.speed}")
print(f"Цвет авто - {my_work.color}")
print(f"Машина полицейская? {my_work.is_police}")
my_work.go()
my_work.stop()
my_work.turn()
my_work.show_speed()

my_police = PoliceCar(40, 'blue', 'kia', True)
print(f"Название автомобиля - {my_police.name}")
print(f"Скорость - {my_police.speed}")
print(f"Цвет авто - {my_police.color}")
print(f"Машина полицейская? {my_police.is_police}")
my_police.go()
my_police.stop()
my_police.turn()
my_police.show_speed()




# Задание 5


class Stationery:
    title = "пишущий инструмент"
    def draw(self):
       print("Запуск отрисовки")
       
class Pen(Stationery):
    def draw(self):
        print("Взяли в руку ручку и начали писать текст")
        
class Pencil(Stationery):
    def draw(self):
        print("Взяли в руку карандаш и поточили его")
        
class Handle(Stationery):
    def draw(self):
        print("Отличный маркер для создания плаката")

my_pen = Pen()
my_pen.draw()

my_pencil = Pencil()
my_pencil.draw()

my_handle = Handle()
my_handle.draw()
















