#  Напишите программу, которая будет преобразовывать десятичное число в двоичное.
    
#     *Пример:*
    
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10

def to_binary(arg):
    binary = ''
    while arg > 0:
        binary +='' + str(arg % 2)
        arg //= 2   
    return binary

x = int(input('>> '))
result = to_binary(x)
print(result[::-1])

