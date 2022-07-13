# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11


def Sum(arg):
    result = 0
    for i in range(0, len(arg)):
        if(arg[i] == '.'):
            continue
        result += int(arg[i])
    return result


number = float(input('Введите число: '))
string_number = str(number)
print(Sum(string_number))

