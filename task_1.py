# Задание 1

user_text = input("Введите текст ")
print(user_text)

user_number = int(input("Введите целое число "))
print(user_number)

# Задание 2

seconds = int(input("Введите количество времени в секундах "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
sec = (seconds % 3600) % 60

print(f"Время: {hours}ч : {minutes}мин : {sec}сек")

# Задание 3

number = int(input("Введите число от 1 до 9 "))

nn = number * 11
nnn = number * 111

sum = number + nn + nnn

print(f"Сумма чисел {number}, {nn}, {nnn} = {sum}")

# Задание 4

number = int(input ("Введите число "))
max = 1
while number > 0:
    a = number % 10
    if a > max:
        max = a
    number = number // 10
print("Максимальная цифра из заданного числа - ", max)

# Задание 5 и 6

proceeds = int(input("Введите сумму вашей выручки "))
cost = int(input("Введите сумму издержки "))

if proceeds > cost:
    rent = (proceeds - cost) / proceeds
    print(f"Вы работаете на прибыль, рентабельность составляет {rent} ")
    staff = int(input("Сколько сотрудников работает у вас на фирме? "))
    earning = (proceeds - cost) / staff
    print(f"Каждый ваш сотрудник получит по {earning} рублей")
elif proceeds == cost:
    print("Вы вышли в ноль")
else:
    print("Вы поработали в убыток(( ")


# Задание 7

current = int(input("Сколько км пробежал спортсмен в первый день? "))
goal = int(input("Сколько км спортсмен хочет пробегать? "))
days = 1
while current < goal:
    current = current + (current / 10)
    days = days + 1
print("Спортсмен достигнет своей цели на ", days, " день")