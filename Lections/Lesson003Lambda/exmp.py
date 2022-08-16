# 
# В файле хранится список чисел от 1 до 100
# Считать список и вывести пары четных чисел и их квадрат

import json

with open('numbers.json','w',encoding='utf-8') as n:
    n.write(json.dumps([i for i in range(1,101)],ensure_ascii=False))
    
with open('numbers.json','r',encoding='utf-8') as file:
    numbers = json.load(file)
    lst = [(i,i**2) for i in numbers if i % 2 == 0 if i < 20]
    
    print(lst) # [(2, 4), (4, 16), (6, 36), (8, 64), (10, 100), (12, 144), (14, 196), (16, 256), (18, 324)]
    
    
def select(f, lst):
    return [f(x) for x in lst]

def where(f, lst):
    return [x for x in lst if f(x)]

data = '1 2 4 6 7 8 9 10 12'.split()

res = select(int, data)

print(res) # [1, 2, 4, 6, 7, 8, 9, 10, 12]

res = where(lambda x: not x%2, res)

print(res) # [2, 4, 6, 8, 10, 12]

res = select(lambda x:(x,x**2),res)

print(res) # [(2, 4), (4, 16), (6, 36), (8, 64), (10, 100), (12, 144)]

