# #1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на нечётной позиции.

#     *Пример:*

#     - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

n = [2, 3, 5, 9, 3]
def sum(n):
    res = 0
    for i in range(1, len(n), 2):
        res += n[i]
    return res

print(sum(n))
