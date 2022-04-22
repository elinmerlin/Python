#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 18:35:21 2022

@author: macbook
"""

# задание 1

from sys import argv

script_name, hours, salary_h, premium = argv
hours, salary_h, premium = int(hours), int(salary_h), int(premium)

def salary(hours, salary_h, premium):
    sal = (hours * salary_h) + premium
    return sal

print(f"Зарплата сотрудника - {salary(hours, salary_h, premium)}")

# задание 2

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list2 = [my_list[x] for x in range(1, len(my_list)) if my_list[x] > my_list[x-1]]
print(my_list2)


# задание 3

my_list = [x for x in range(20, 241) if x % 20 == 0] 
print(my_list)

# задание 4 

first_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
second_list = [x for x in first_list if first_list.count(x) == 1]
print(second_list)


# задание 5

from functools import reduce
my_list = [x for x in range(100, 1001) if x % 2 == 0]
def my_func(prev_el, el):
    result = prev_el * el
    return result 

print(reduce(my_func, my_list))


# задание 6

from itertools import count

for el in count(4):
    if el > 10:
        break
    else:
        print(el)
   

from itertools import cycle

с = 0
for el in cycle([5, 7 , 6]):
    if с > 5:
        break
    else:
        print(el)
        с += 1


# задание 7

from math import factorial
n = int(input("Введите число "))
def fact(n):
    for el in range(1, n+1):
        yield factorial(el)   

for el in fact(n):
    print(el)

