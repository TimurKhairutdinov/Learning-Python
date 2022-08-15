# Работа с файлами


color = ['Red', 'Green', 'Blue3']

# Создаем переменую и связываем с текстовым файлом.
data = open('file.txt', 'a')

# Запись данных
data.writelines(color)  # Разделителей не будет
data.write('\nnumbers = ')
data.write('4\n')

# # Закрытие подключения к файлу
data.close()


# # exit() - позволяет не выполнять код, который написан ниже.


with open('file.txt', 'a') as data:
    data.write('numbers4 = ')
    data.write('452')

path = 'file.txt'
data = open(path, 'r+')
for line in data:
    print(line)
data.close()
