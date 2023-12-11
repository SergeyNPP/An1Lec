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

# Управляющие конструкции: if, if-else
# Управляющие конструкции: while и вариация while-else
# Цикл for, range
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