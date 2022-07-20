# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.


def check_number(list):
    for i in list:
        if i.isdigit():
            return i


str = 'В Петербурге сегодня солнечно, 23 градуса тепла'
ls = str.split()  # list
print(check_number(ls))
