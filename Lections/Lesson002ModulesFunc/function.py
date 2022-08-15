# Функции

import Files as fs

print(fs.color)

# Значения по умолчанию
def new_string(symb, count=3):
    return symb*count


print(new_string('!', 5))   # !!!!!
print(new_string('!'))  # !!!
print(new_string(5))    # 15

# Неограниченное количество аргументов
def concantenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res


def concantenatio_int(*params):
    res: int = 0
    for item in params:
        res += item
    return res


print(concantenatio('a', 'b', 'c', 'd', 'e', 'f'))  # abcdef
print(concantenatio('1', '2', '3', '4', '5', '6'))  # 123456
print(concantenatio_int(1, 2, 3, 4, 5, 6))  # 21

