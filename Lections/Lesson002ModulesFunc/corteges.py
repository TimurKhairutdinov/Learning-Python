# Кортежи - неизменяемые списки

# type = tuple

t = ()
print(type(t))  # tuple

t = (1,)
print(type(t))  # tuple

t = (1)
print(type(t))  # int

t = (28, 9, 199)
print(type(t))  # tuple

colors = ['red', 'green', 'blue']

t = tuple(colors)
print(t)
print(type(t))  # tuple

a = 3, 4
print(type(a))  # tuple
print(a[1])  # 4
a, b, c = 1, 2, 3
a = (a, b, c)
print(a)    # (1,2,3)
print(type(a))  # tuple

for item in a:
    item += item 
    print(item)  # 2 4 6

color = ['Red', 'Green', 'Blue']
corteg = tuple(color)
print(corteg)   #
print(type(corteg))  # tuple

red, green, blue = corteg # Распаковка кортежа
print(f'r: {red}, g: {green}, b: {blue}')  # r: Red, g: Green, b: Blue
