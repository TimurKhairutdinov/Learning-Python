# Управляющие конструкции
# if, if-else

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))

if a > b:
    print(a)
else:
    print(b)

# elif

username = input('Введите имя: ')
if username == 'Маша':
    print('Ура это Маша!')
elif username == 'Марина':
    print('Мы вас ждали Марина!')
else:
    print('Привет,', username)
