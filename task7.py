# задание 1

class Matrix:
    def __init__(self, matrix1):
        self.matrix1 = matrix1
       
    def __str__(self):
        res1 = ''
        for el in self.matrix1:
            l = " ".join(map(str, el)) + '\n'
            res1 += l
        return f"matrix:\n{res1}"           #надеюсь, это имеется в виду под "привычном видом" матрицы
    
    def __add__(self, other):
        res = []
        for el in range(len(self.matrix1)):
            s = [x + y for x, y in zip(self.matrix1[el], other.matrix1[el])]
            res.append(s)
        return res
                
my_matrix = Matrix([[1, 45, 32],
                    [2, 32, 2],
                    [23, 90, 8]])
my_matrix2 = Matrix([[7, 6, 8],
                     [7, 5, 0],
                     [3, 7, 9]])

print(my_matrix)

print(f"Сумма двух матриц - {my_matrix + my_matrix2}")

# задание 2

from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        super().__init__()
    @abstractmethod
    def get_fabric(self):
        pass
    
    
class Coat(Clothes):
    
    def __init__(self, size):
        self.v = size
    @property   
    def get_fabric(self):
        return f'Расход ткани - {round(self.v/6.5 + 0.5, 2)}'
        
class Suit(Clothes):
    
    def __init__(self, hight):
        self.h = hight 
    @property
    def get_fabric(self):
        return f'Расход ткани - {round(2*self.h + 0.3, 2)}'

size = int(input("Введите размер пальто "))
my_coat = Coat(size)  
print(my_coat.get_fabric)
        
hight = int(input("Введите рост для костюма "))
my_suit = Suit(hight)  
print(my_suit.get_fabric)  
        
  
# задание 3

class Cell:
    
    def __init__(self, cellule):
        self.cellule = cellule
        
    def __add__(self, other):
        return self.cellule + other.cellule
    
    def __sub__(self, other):
        if self.cellule > other.cellule:
            return self.cellule - other.cellule 
        else:
            return "Количество ячеек первой клетки меньше ячеек второй"
        
    def __mul__(self, other):
        return self.cellule * other.cellule
    
    def __truediv__(self, other):
        return self.cellule // other.cellule
    
    def make_order(self, numb_in_order):
        try:
            block = ['*' for x in range(numb_in_order)]
            block = ''.join(block) + '\n'
            res = [block for x in range(self.cellule // numb_in_order)]
            block2 = ['*' for x in range(self.cellule % numb_in_order)]
            return ''.join(res) + ''.join(block2)
        except ZeroDivisionError:
            return "Нельзя задать 0 ячеек!"
        
first_cell = Cell(100)
second_cell = Cell(20)

print(f"Сумма ячеек - {first_cell + second_cell}")
print(f"Разница ячеек - {first_cell - second_cell}")
print(f"Произведение ячеек - {first_cell * second_cell}")
print(f"Резултат деления ячеек - {first_cell / second_cell}")

numb_in_or = int(input("Введите количество ячеек в ряду "))
print(first_cell.make_order(numb_in_or))














