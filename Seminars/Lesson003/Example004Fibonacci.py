# Задайте список из n чисел ряда фибоначчи
n = 5
lst = []


def Fib(arg, lst):
    i = 0
    while i < arg:
        if i == 1 or i == 2:
            return lst.append(1)
        elif i == 2:
            return lst.append(2)
        else:
            return lst.append(i-1+i+2)


print(Fib(n,lst))

def fibo(n):
    if n in [1,2]:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

x = int(input('Введите число элементов: '))

def fibolist(x):
    list = []
    for i in range(1, x+1):
        list.append(fibo(i))
    return list
print(fibolist(x))

