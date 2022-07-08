# Списки введение
## list = list

# Список
numbers = [1, 2, 3, 4, 5]
print(numbers)

ran = range(-5, 6)
print(ran)  # range(-5, 6)
print(type(ran))  # type 'range', note list.

numbers = list(ran)
print(numbers)  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
print(type(numbers))  # type 'list'

print(f'len {len(numbers)}')  # 11

numbers[5] = 10
print(numbers)  # [-5, -4, -3, -2, -1, 10, 1, 2, 3, 4, 5]

for i in numbers:
    i *= 2
    print(i)    # -10 -8 -6 -4 -2 20 2 4 6 8 10
print(numbers)  # [-5, -4, -3, -2, -1, 10, 1, 2, 3, 4, 5]

###

colors = ['red', 'green', 'blue']

for e in colors:
    print(e)    # red green blue

for e in colors:
    print(e*2)  # blue redred greengreen blueblue

colors.append('gray')   # Добавить в конец 
print(colors)   # ['red', 'green', 'blue', 'gray']

print(colors == ['red', 'green', 'blue', 'gray']) # True

colors.remove('green') # Удалить элемент green
print(colors)   # ['red', 'blue', 'gray']

del colors[1]   # Удалить элемент 1
print(colors)   # ['red', 'gray']