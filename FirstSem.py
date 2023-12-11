# Отступы в Python играют огромную роль, стоит Вам поставить на 1 пробел меньше,
# чем нужно, Ваша программа будет не рабочая.
# Отступом отделяется блок кода, который находится внутри операторов ветвления,
# циклов, функций и тд

# Операторы ввода и вывода данных
# Логические операции

# 1. Возведение в степень (**)       iter **= 5  iter = iter ** 5 
# 2. Умножение (*)                   iter *= 5  iter = iter * 5
# 3. Деление (/)                     iter /= 5  iter = iter / 5
# 4. Целочисленное деление (//)      iter //= 5  iter = iter // 5
# 5. Остаток от деления (%)          iter %= 5  iter = iter % 5
# 6. Сложение (+)                    iter += 3  iter = iter + 3
# 7. Вычитание (-)                   iter -= 4  iter = iter - 4

# Знак операции Операция
# > Больше
# >= Больше или равно
# < Меньше
# <= Меньше или равно
# == Равно (проверяет, равны ли числа)
# != Не равно (проверяет, не равны ли значения)
# not Не (отрицание)
# and И (конъюнкция)
# or Или (дизъюнкция)

# Управляющие конструкции: if, if-else                                  строка 148
# Управляющие конструкции: while и вариация while-else                  строка 168
# Цикл for, range                                                       строка 212
# Срезы 

# print(5, 5,3)

# n = 5
# print(n)

# Для присваивания пустого значения
#  n = None #ВАЖНО! если сделать отступ (пробел) перед n, то ПРОГРАММА РАБОТАЕТ НЕКОРРЕКТНО!
# print(n)

# n = 5
# print(n)
# n = "Sergey"  #Для вывода текста ОБЯЗАТЕЛЬНЫ КОВЫЧКИ
# print(n)

# n = 5
# print(type(n)) 
# Выводится <class 'int'>
# n = wrwer
# print(type(n)) 
# Выводится <class 'str'>
# n = 'fr\'rfr'             или  n = 'fr"'"rfr' Двойные ковычки
# print(n) 
# Выводится fr'rfr

# a = 5
# b = 4.323
# c = 'Hey'
# print(f"{a} - {b} - {c}") # обязательно ф и ковычки
# или
# print("{} - {} - {}".format(a,b,c))
# Выводится 5 - 4.323 - Hey

# print ('Введите первую строку')
# a = input() 
# Выводится Введите первую строку
#           54
# b = input('Введи 2 строку ')
# Выводится Введи 2 строку 46

# print ('Введите первую строку')
# a = input() 
# b = input('Введи 2 строку ')
# print(a,'+', b,'=',a+b)
# Выводится
# Введите первую строку
# 45
# Введи 2 строку 15
# 45 + 15 = 4515

# c = 4.342
# print(c)
# n = int(c)
# print(n)
# Выводится
# 4.342
# 4

# c = 4.342
# print(type(c))
# print(c)
# c = int(c)
# print(type(c))
# print(c)
# Выводится
# <class 'float'>
# 4.342
# <class 'int'>
# 4

# c = 4.342
# print(type(c))
# print(c)
# c = str(c)
# print(type(c))
# print(c + 'sdq')
# Выводится
# <class 'float'>
# 4.342
# <class 'str'>
# 4.342sdq

# print ('Введите первую строку')
# a = int(input())
# b = int(input('Введи 2 строку '))
# print(a,'+', b,'=',a+b)
# Выводится
# Введите первую строку
# 4
# Введи 2 строку 6
# 4 + 6 = 10

# a = 3.23113
# b = 2.4552
# print(round(a*b, 3))


# a = 1 > 4
# print(a) # False

# a = 1 < 4 and 5 > 2
# print(a) # True

# a = 1 == 2
# print(a) # False

# a = 1 != 2
# print(a) # True

# a = 'qwe'
# b = 'qwe'
# print(a == b) # True

# a = 1 < 3 < 5 < 10
# print (a) # True

# if condition:
#   operator 1
#   operator 2
#   ...
#   operator n
# else:
#   operator n + 1
#   operator n + 2
#   ...
#   operator n + m

# if condition1:
#   operator
# elif condition2:
#   operator
# elif condition3:
#   operator
# else:
#   operator

# while condition:
#   operator 1
#   operator 2
#   ...
#   operator n

# n = 423
# summa = 0
# while n > 0:
# x = n % 10
# summa = summa + x
# n = n // 10
# print(summa) # 9


# while condition:
#  operator 1
#   operator 2
#   ...
#   operator n
# else:
#   operator n + 1
#   operator n + 2
#   ...
#   operator n + m

# Блок else выполняется, когда основное тело цикла перестает работать
# самостоятельно. Внутри Python break

#             найти минимальный делитель данного числа

# n = int(input())
# flag = True
# i = 2
# while flag:
# if n % i == 0: # если остаток при делении числа n на i равен 0
# flag = False
# print(i)
# elif i > n // 2: # делить числа не может превышать введенное число, деленное
# на 2
# print(n)
# flag = False
# i += 1

# for i in enumeration:
#  operator 1
#   operator 2
#   ...
#   operator n
# for i in 1, -2, 3, 14, 5:
# print(i)
#   1 -2 3 15 5

# Range
# ● Range выдает значения из диапазона с шагом 1.
# ● Если указано только одно число — от 0 до заданного числа.
# ● Если нужен другой шаг, третьим аргументов можно задать приращение.
# r = range(5) # 0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(-5, 0) # ----
# r = range(1, 10, 2) # 1 3 5 7
# r = range(100, 0, -20) # 100 80 60 40 20
# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r:
# print(i)
# # 100 80 60 40 20

# for i in 'qwerty':
# print(i)
#   q
#   w
#   e
#   r
#   t
#   y

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)
# выводит 
# *****
# *****
# *****
# *****
# *****

# Команды для работы со строками:
# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# 1. Определить количество символов в строке:
# print(len(text)) # 39
# 2. Проверить наличие символа в строке (in):
# print('ещё' in text) # True
# 3. Функция, которая делает все буквы строки маленькими:
# print(text.lower()) # съешь ещё этих мягких французских булок
# 4. Функция, которая делает все буквы строки большими:
# print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
# 5. Заменить слово на другое :
# print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок

# Срезы
# ● Мы представляем строку в виде массива символов. Значит мы можем обращаться к элементам по индексам.

# ● Отрицательное число в индексе — счёт с конца строки
# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ

# print(text[len(text)-1]) # к
# print(text[-1]) # к

# print(text[:]) # съешь ещё этих мягких французских булок
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...