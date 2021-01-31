# #   УГАДАЙ ЧИСЛО:
#
# number = 43
# value = int(input('Угадайте число от 1 до 100 '))
# while value != number:
#     if value < number:
#         print('Загадано число поболее')
#         value = int(input('Угадайте число от 1 до 100 '))
#     if value > number:
#         print('Загадано число поменьше')
#         value = int(input('Угадайте число от 1 до 100 '))
# if value == number:
#     print('Верно, загадано число', number)
###################################

#   ВЫВОД ЧИСЕЛ ОТ 0 ДО 100:

# number = 0
# while number <= 10:
#     print(number)
#     # number = number + 1
#     number += 1
###################################

#   ВЫВОД ЧИСЕЛ ОТ 0 ДО N:

# number = 0
# n = int(input('Введите число от 0 до которого будем выводить.\n От 0 до: '))
# while number <= n:
#     print(number)
#     # number = number + 1
#     number += 1
###################################

#   ВЫВОД ЧЕТНЫХ ЧИСЕЛ ОТ 0 ДО N:
# number = 0
# n = int(input('Введите число от 0 до которого будем выводить четные числа: '))
# while number <= n:
#     if number % 2 == 0:
#         print(number)
#     # number = number + 1
#     number += 1
###################################

#   BREAK
# name = None
# while name != 'Гвидо' or name != 'Gvido':
#     name = input('Кто создатель Python? ')
#     if name == 'Гвидо' or name == 'Gvido':
#         break
#     print('Не верно')
#
# print('Верно')

# Другой вариант через True
# name = None
# while True: # Пhи таком условии обязательно должен быть выход BREAK
#     name = input('Кто создатель Python? ')
#     if name == 'Гвидо' or name == 'Gvido':
#         break
#     print('Не верно')
#
# print('Верно')
###################################

#   CONTINUE
# number = 0
# n = int(input('Введите число от 0 до которого будем выводить четные числа: '))
# while number <= n:
#     if number % 2 != 0:
#         number += 1
#         continue # В данном случае пропускает нечетные числа
#     print(number)
#     number += 1
###################################

#   WHILE-ELSE
# number = 0
# while number <= 10:
#     print(number)
#     number += 1
#     # if number == 5:
#     #     break
# else:
#     print('end-end')
#
# print('END')
###################################


# ДОМАШКА
# 1. Прибавляем 2
# number = int(input('Введите число: '))
# sum = number + 2
# print(f'Если к Вашему числу {number} прибавить 2 получится: {sum}')

# ЦИКЛ (тварь)
# stp = "при возведении в степень 2"
# while True:
#     number = int(input('Введите число от 1 до 10: '))
#     if number <= 0 or number >= 10:
#         print('Число неверное, введите число от 1 до 10')
#     else:
#         print(number ** 2, stp)
#         break

# 3. Анкета
# name = input('Введите Ваше имя: ')
# surname = input('Введите Вашу фамилию: ')
# age = int(input('Сколько Вам лет: '))
# weight = int(input('Сколько Вы весите: '))
#
# if age <= 30 and weight >= 50 and weight <= 120:
#     print(name, surname, ', Вы в хорошем состоянии')
# elif age >= 30 and age <= 40 and weight >= 120 or weight <= 50:
#     print(name, surname, ', Вам бы заняться собой')
# elif age >= 40 and weight >= 120 or weight <= 50:
#     print(name, surname, ', Вам хана')
