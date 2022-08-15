# Множества
# base api

# *-------------------------------------------*

# colors = {'red', 'green', 'blue'}

# print(colors)   # {'green', 'red', 'blue'}
# print(type(colors)) # <class 'set'>

# colors.add('gray') 
# print(colors)   # {'green', 'red', 'blue', 'gray'}

# colors.remove('red') 
# print(colors) # {'gray', 'blue', 'green'}
# # colors.remove('red') KeyError: 'red'

# colors.discard('red') # Не вызывет ошибку, если элемент отсутствует

# colors.clear() # { }
# print(colors) # set()

# *-------------------------------------------*

a = {1,2,3,5,6,8,9,12}
b = {2,5,7,10,21,24}

c = a.copy() # Копирует множество
print(c) # {1, 2, 3, 5, 6, 8, 9, 12}

u = a.union(b) # Объединение множеств 
print(u) # {1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 21, 24}

i = a.intersection(b) # Пересечение двух множеств 
print(i) # {2, 5}

da = a.difference(b) # Разница множества a от b
print(da) # {1, 3, 6, 8, 9, 12}

db = b.difference(a) # Разница множества b от a
print(db) # {24, 10, 21, 7}
print('q')
q = (a \
    .union(b) \
    .difference(a.intersection(b)))
print(q) # {1, 3, 6, 7, 8, 9, 10, 12, 21, 24}
# *-------------------------------------------*

# Не изменяемые множества (Замороженные)
s = frozenset(a)
print(s) # frozenset({1, 2, 3, 5, 6, 8, 9, 12})
print(type(s)) # <class 'frozenset'>

# *-------------------------------------------*

