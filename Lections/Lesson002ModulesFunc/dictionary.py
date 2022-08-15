
# Словари
# Неупорядоченные коллекции произвольных объектов с доступом по ключу

dictionary = {}
dictionary = \
    {
        'one': '1',
        'two': '2',
        'three': '3',
        'third': '4'
    }
print(dictionary)   # {'one': '1', 'two': '2', 'three': '3', 'third': '4'}
print(type(dictionary))  # dict
print(dictionary['two'])  # 2
# Типы ключей могут отличаться


print(dictionary.keys())
for i in dictionary.keys():
    print(i)  # one two three third

print(dictionary.values())
for i in dictionary.values():
    print(i)  # 1 2 3 4

# dict_items([('one', '1'), ('two', '2'), ('three', '3'), ('third', '4')])
print(dictionary.items())

print(dictionary.get('one'))  # 1

print(dictionary.fromkeys('two', 5))
print(dictionary)
dictionary['one'] = 90  # Изменение значения
dictionary['two'] = 120
# Если ключа не существует в текущем словаре, он его добавит
dictionary['five'] = 5
print(dictionary)


# dictionary.clear()  # очистка словаря
print(dictionary)  # {}
# ____________________________________ #
# del dictionary  # Удаление словаря
print(dictionary)  # NameError: name 'dictionary' is not defined

res = {}
res['Слово1'] = 5
res['Слово22'] = 0
res['Слово3'] = 0

temp = res.get('Слово1')
temp += 2
res['Слово1'] = temp

print(res.get('Слово1'))
# print(dictionary.fromkeys('two', 5))

print(dictionary)
dictionary.pop('five')
print(dictionary)