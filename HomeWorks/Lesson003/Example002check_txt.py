# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:

# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
import json

def check_text(line, find):
    count = -1
    for i in range(len(line)):
        if find == line[i]:
            index = i
            count += 1
            if count == 1:
                return index
    if count < 1:
        return -1


list = [1992, 1995, 1993, 1996, 2001, 1999]

print(check_text(list, 1992))

