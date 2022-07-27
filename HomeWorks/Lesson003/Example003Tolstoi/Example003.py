# 3* (необзательная).
# Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.

# Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом
# и вывести получившуюся статистику.

# Программа должна считывать одну строку со стандартного ввода
# и выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра)
# в формате "слово количество" (см. пример вывода).
# Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться только один раз.

import json
import re


def d(list):
    dict = {}
    c = len(list)
    for i in list:
        dict[i] = 0
        c -= 1
        print(f'{c}: dict d {i}')
    print('d complete!')
    return dict


def check(list):
    dict = d(list)
    c = len(list)
    for i in list:
        for j in dict.keys():
            if i == j:
                temp = dict.get(i)
                temp += 1
                dict[i] = temp
                c -= 1
                print(f'{c}: check dict {i}')
    print('check complete!')
    return dict


text = ''
with open('text.txt', 'r', encoding='utf-8') as data:
    for line in data:
        text += ' ' + line.lower() 
        print(f'text + done {line}')
    print('Open complete!')

ls = text.split()

with open('result.json', 'w', encoding='utf-8') as fh:
    fh.write(json.dumps(check(ls), ensure_ascii=False))
    print('result complete!')
