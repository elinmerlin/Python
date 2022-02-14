# Задание 1

from datetime import datetime

class Data:
    
    def __init__(self, data):
        self.data = data
        
    @classmethod
    def get_numb_data(cls, param):
        my_date = datetime.strptime(param, "%d-%m-%Y")
        print(f"Дата - {datetime.date(my_date)}, год - {my_date.year}, месяц - {my_date.month}, день - {my_date.day}") 
    # В методичке как-то непонятно написано, что нужно дать на выходе, я решила сделать вот так
    
    @staticmethod
    def data_validation(param):
        try:
            datetime.strptime(param, "%d-%m-%Y")
            Data.get_numb_data(str_data)
            print("Дата введена правильно")
        except ValueError: 
            print("Введите дату в правильном формате: номер месяца не должен быть более 12, а количество дней не должно превышать количество дней в заданном месяце!")
 
str_data = input("Введите дату в формате день-месяц-год цифрами ")
Data.data_validation(str_data)


# задание 2

class My_error(Exception):
    def __init__(self, txt):
        self.txt = txt
        
class Devision:
    def __init__(self, my_input):
        self.input = my_input
        
    def devide(self):
        try:
            if self.input == 0:
                raise My_error ("На ноль делить нельзя!")
            else:
                print(f"Результат деления 10 на {self.input} = {round(10 / self.input, 2)}")
        except My_error as err:
            print(err)
            
my_input = int(input("Введите число "))
a = Devision(my_input)
a.devide()


# Задание 3

class My_exception(Exception):
    pass

my_list = []

while True:
    try:
        number = input("Введите число, для остановки напишите 'stop' ")
        if not number.isdigit() and number != 'stop':
            raise My_exception
        if number != 'stop':
            my_list.append(int(number))
        else:
            print(f"Ввод окончен, список введенных чисел - {my_list}")
            break
    except My_exception:
        print("Вводить можно только числа ")

# Задание 4, 5, 6 



from abc import ABC, abstractmethod

class Warehouse(ABC):
    @abstractmethod
    def __init__(self):
        super().__init__()
    @abstractmethod
    def get_equipment(cls):
        pass
    @abstractmethod
    def equipment_distribution(cls):
        pass
    
class Office_equipment(Warehouse):
    def __init__(self, name, color):
        self.name = name
        self.color = color
    @classmethod
    def get_equipment(cls):
        try:
            cls.pr_number = int(input("Введите количество закупленных принтеров "))
            cls.sc_number = int(input("Введите количество закупленных сканеров "))
            cls.x_number = int(input("Введите количество закупленных ксероксов "))
            cls.numbers = {'printers' : cls.pr_number, 'scaners' : cls.sc_number, 'xerox' : cls.x_number}
            print(f"Поступление оргтехники: {cls.numbers}")
            Office_equipment.equipment_distribution()
        except ValueError:
            print("Количество техники задавать числом ")
    @classmethod
    def equipment_distribution(cls):
            print(f"Первое подразделение получает {cls.pr_number//2} принтеров, {cls.sc_number//2} сканеров, {cls.x_number//2} ксероксов. \n"
                  f"Второе подразделение получает {cls.pr_number - cls.pr_number//2} принтеров, {cls.sc_number - cls.sc_number//2} сканеров, {cls.x_number - cls.x_number//2} ксероксов.")
            
class Printer(Office_equipment):
    def __init__(self, name, color, type_of_printer):
        super().__init__(name, color)
        self.type_of_printer = type_of_printer
    def __str__ (self):
        return f"Техника: {self.color} {self.name}, тип - {self.type_of_printer}"
    
class Scaner(Office_equipment):
    def __init__(self, name, color, maker):
        super().__init__(name, color)
        self.maker = maker
    def __str__ (self):
        return f"Техника: {self.color} {self.name}, производитель - {self.maker}"

class Xerox(Office_equipment):
    def __init__(self, name, color, year):
        super().__init__(name, color)
        self.year = year
    def __str__ (self):
        return f"Техника: {self.color} {self.name}, год производства - {self.year}"


pr_name = input("Введите название приентера ")
pr_color = input("Введите цвет принтера ")
pr_type = input("Введите тип принтера ")
my_printer = Printer(pr_name, pr_color, pr_type)
print(my_printer)

sc_name = input("Введите название сканера ")
sc_color = input("Введите цвет сканера ")
sc_maker = input("Введите производителя сканера ")
my_scaner = Scaner(sc_name, sc_color, sc_maker)
print(my_scaner)

x_name = input("Введите название ксерокса ")
x_color = input("Введите цвет ксерокса ")
x_year = input("Введите год производства ")
my_xerox = Xerox(x_name, x_color, x_year)
print(my_xerox)

Office_equipment.get_equipment()


# задание 7


class Complex_numbers():
    def __init__(self, a, b):
        self.a = a
        self.b = b 
        
    def __add__(self, other):
        return f"{self.a + other.a} + {self.b + other.b}i"
    
    def __mul__(self, other):
        a = self.a * other.a
        b = self.a * other.b + self.b * other.a 
        c = self.b * other.b * (-1)
        return f"{a + c} + {b}i"
        
a1 = int(input("Для комплексного числа z = a + bi введите знаечние a "))
b1 = int(input("Для комплексного числа z = a + bi введите знаечние b "))
c1 = Complex_numbers(a1, b1)

a2 = int(input("Для второго комплексного числа z = a + bi введите знаечние a "))
b2 = int(input("Для второго комплексного числа z = a + bi введите знаечние b "))
c2 = Complex_numbers(a2, b2)

print(f"Сумма комплексных чисел {a1} + {b1}i и {a2} + {b2}i равна {c1 + c2}\n"
      f"Произведение равно = {c1 * c2}")





























