# Ввод и вывод данных
# print, input

# input по умолчанию имеет тип строки str
# int() Конвертирует в целочисленный тип
# float() Конвертирует в вещественный тип

print('Введите число a: ')
a = int(input())
print('Введите число b: ')
b = float(input())

print(a, '-', type(a))
print(b, '-', type(b))
print('{} {}'.format(a, b))
print(f'{a} + {b} = {a+b}')
