# 32. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.



lst = [5, 3, 22, 66, 2, 55, 1, 4, 6, 3, 4, 5, 1, 3, 7, 8, 8, 9, 5, 9, 1, 0]

# 1
print(list(filter(lambda i: lst.count(i) == 1, lst)))

# 2

print([i for i in lst if lst.count(i)==1])

