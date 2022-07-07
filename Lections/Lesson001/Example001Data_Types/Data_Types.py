
# Типы данных и переменные
# int, float, str, boolean, lists, None

a = 12
b = 1.2
name = 'Timur'
bool = False
list = [1, 2, 3, 4, 5]
value = None

print(f'{a} - {type(a)}')
print(f'{b} - {type(b)}')
print(f'{name} - {type(name)}')
print(f'{bool} - {type(bool)}')
print(f'{list} - {type(list)}')
print(f'{value} - {type(value)}')

# Строки
s = "Hello World"
n = 'Hello \nWorld'
s1 = '"Hello World"'
s2 = "'Hello World'"

print(s)
print(n)
print(s1)
print(s2)

# Вывод
print(a, b, name)
print(a, '-', b, '-', name)
print('{} - {} - {}'.format(a, b, name))

# Интерполяция
print(f'{a} - {b} - {name}')
print('{2} - {0} - {1}'.format(a, b, name))

# Списки - это как массивы только круче

list1 = [1, 2, 3, 4, 5]
list2 = [1, a, b, name, bool, value]

print(list1)
print(list2)

