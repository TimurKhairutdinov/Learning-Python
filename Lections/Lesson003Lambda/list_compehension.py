# List Comprehension
# Базовые конструкции\
# [exp for item in itarable]
# [exp for item in itarable if conditional]
# [exp <if conditional> for item in itarable if conditional]

lst = []
for i in range(1,11):
    lst.append(i)
print(lst) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst = [i for i in range(1,11)]
print(lst) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Как видно, результат заполнения будет идентичным.

# Добавим условие

lst = [i for i in range(1,11) if i%2==0]
print(lst) # [2, 4, 6, 8, 10]

# Добавим кортежи
lst = [(i-1, i) for i in range(1,11) if i%2==0]
print(lst) # [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

# Добавим фукнцию lambda
f = lambda i: i**3
lst = [(i, f(i)) for i in range(1,11) if i%2 == 0]
print(lst) # [(2, 8), (4, 64), (6, 216), (8, 512), (10, 1000)]
# *-------------------------------------------------------*
