# Задача 17. Напишите программу, которая принимает на вход координаты точки (x,y),
# причём x != 0, y != 0,
# и выдаёт номер четверти плоскости, в которой находится эта точка.
#     Y
#  1  |  2
# ____|____ X
#     |
#  3  |  4
#

def GetCoordinate(x, y):
    if x == 0 or y == 0:
        print("error - (0,0)")
    elif x < 0 and y > 0:
        return 1
    elif x > 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4


x = int(input('Введите x: '))
y = int(input('Введите y: '))

print(f'Точка находится в чеверти номер: {GetCoordinate(x, y)}')
