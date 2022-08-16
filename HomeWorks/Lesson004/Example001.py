# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def pr(n):
    res = []
    for i in range(1, n+1):
        if (n % i == 0):
            res.append(i)
    return res

number = int(input('Введите натуральное число: '))

print(pr(number))
