# Задачи:
# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
#     *Примеры:* 
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет

num_one = int(input('Введите первое число: '))
num_two = int(input('Введите второе число: '))

if num_one == num_two**2:
    print('Да!')
elif num_two == num_one**2:
    print('Да!')
else: print('Нет!')