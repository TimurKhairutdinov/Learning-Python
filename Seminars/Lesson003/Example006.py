# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# сохраните список в формате JSON.
import json
from Example007WriteFile import WriteJSON



def Magic(arg):
    return list(range(-arg, arg+1))


n = int(input('Введите число: '))
result = (Magic(n))


with open('list.json', 'w', encoding='utf-8') as ls:
    ls.write(json.dumps(result, ensure_ascii=False))
print('Результат сохранён.')

WriteJSON(ls)
print(type(ls))
