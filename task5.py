# задание 1

obj = open("text.txt", 'w')
while True:
    new_line = input("Введите новую строку ")
    new_line1 = new_line + "\n"
    obj.write(new_line1)
    if not new_line:
        obj.close()
        print("Ввод текста закончен")
        break

# Для проверки записанного в новый файл
for_checking = open('text.txt', encoding = 'utf-8')
check = for_checking.read()
print(check)
for_checking.close()

# задание 2

out_f = open("testElina1.txt", "w")
str_list = ['привет мир\n', 
            'посмотри на звезды\n', 
            'однажды мы разгадаем тайны Вселенной\n']
out_f.writelines(str_list)
out_f.close()

my_file = open("testElina1.txt")
content = my_file.readlines()
print(f"Количество строк в файле = {len(content)}")
words = []
for line in content:
    words.append(len(line.split()))
print(f"Количество слов в строках соответственно = {words}")


# задание 3 

out_f = open("testElina.txt", "w")
str_list = ['Иван 10000\n', 
            'Петр 100\n', 
            'Алена 20000\n', 
            'Марина 500000\n', 
            'Артем 12\n', 
            'Кирилл 70000\n', 
            'Арсений 9999\n', 
            'Михаил 100000\n', 
            'Авазбек 50000\n', 
            'Милана 12890\n']
out_f.writelines(str_list)
out_f.close()

from statistics import mean 
salary = open("testElina.txt", 'r', encoding = 'utf-8')
salary = salary.readlines()
high_sal = [x.split()[0] for x in salary if int(x.split()[1]) < 20000]
print(f"Сотрудники с зп более 20к: {high_sal}")
average = [x.split()[1] for x in salary]
average = mean(map(int, average))
print(f"Средняя зарплата сотрудника - {average}")
  

# задание 4 - с загрузкой библиотеки, но работает медленно

from translate import Translator

out_f = open("testElina2.txt", "w")
str_list = ['One — 1\n', 
            'Two — 2\n', 
            'Three — 3\n',
            'Four — 4']
out_f.writelines(str_list)
out_f.close()

new_file = open('testRussian.txt', 'a')

with open("testElina2.txt", encoding = 'utf-8') as file:
    for line in file:
        translator = Translator(to_lang="Russian")
        translation = translator.translate(line)
        print(translation)
        new_file.write(translation + '\n')

new_file.close()

#задание 4 - решение без новых библиотек, но решение некрасивое(((

out_f = open("testElina2.txt", "w")
str_list = ['One — 1\n', 
            'Two — 2\n', 
            'Three — 3\n',
            'Four — 4']
out_f.writelines(str_list)
out_f.close()

new_file = open('testRussian.txt', 'a')

with open("testElina2.txt", encoding = 'utf-8') as file:
    for line in file:
        if line == ('One — 1\n'):
            print('один - 1')
            new_file.write('один - 1\n')
        elif line == ('Two — 2\n'):
            print('два - 2')
            new_file.write('два - 2\n')
        elif line == ('Three — 3\n'):
            print('три - 3')
            new_file.write('три - 3\n')
        else:
            print('четыре - 4')
            new_file.write('четыре - 4\n')

new_file.close()

# Для проверки записанного в новый файл
#for_checking = open('testRussian.txt', encoding = 'utf-8')
#check = for_checking.read()
#print(check)
#for_checking.close()

#Задание 5


out_f = open("testElina3.txt", "w")
out_f.write('786 765 3 87')
out_f.close()

with open("testElina3.txt") as numb:
    numbers = numb.read()
    result = [int(x) for x in numbers.split()]
    print(f"Сумма всех чисел в файле = {sum(result)}")


# Залание 6

out_f = open("testElina4.txt", "w")
str_list = ['Информатика: 100 (л) 50 (пр) 20 (лаб),\n Физика: 30 (л) — 10 (лаб),\n Физкультура: — 30 (пр) —']
out_f.writelines(str_list)
out_f.close()

my_value = []
my_keys = []
subj = open("testElina4.txt", encoding = 'utf-8')
for line in subj:
    summa = sum([int(x) for x in line.split() if x.isdigit()])
    my_value.append(summa)
    names = line.split(':')[0]
    my_keys.append(names)
my_dict = dict(zip(my_keys, my_value))
print(my_dict)

# задание 7

from statistics import mean 
import json

out_f = open("testElina5.txt", "w")
str_list = ["фирма1 ООО 1000 60\n"
            "фирма2 ОАО 500 6000\n"
            "фирма3 ООО 20000 6000"]
out_f.writelines(str_list)
out_f.close()

profit = []
firms = []
with open("testElina5.txt", encoding = 'utf-8') as info:
    for line in info:
        pr = line.split()
        a = int(pr[2]) - int(pr[3])
        profit.append(a)
        firms.append(pr[0])
        
positive_profit = [x for x in profit if x > 0]
average_profit = mean(positive_profit)
dict1 = dict(zip(firms, profit))
dict2 = {'average profit' : average_profit}
result_list = [dict1, dict2]
print(result_list)

with open("my_file.json", "w") as write_f:
    json.dump(result_list, write_f)

# для проверки записанного в json
#with open("my_file.json") as read_f:
#    data = json.load(read_f)

#print(data)














