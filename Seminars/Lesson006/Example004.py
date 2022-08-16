# 4. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

# *Пример:* 

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]



def return_unique(lst):
  return [i for i in lst if lst.count(i)==1]


lst = list(map(int, '1, 2, 3, 5, 1, 5, 3, 10'.split(',')))
print(f"Список из неповторяющихся элементов: {return_unique(lst)}")