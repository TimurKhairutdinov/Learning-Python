# 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
import json

def func(numbers):
    res = []
    for i in range(1, len(numbers)):
        if numbers[i] - 1 != numbers[i-1]:
            res.append(numbers[i]-1)
    return res
    

with open('task35.json', 'r', encoding='utf-8') as f:
    lst = json.load(f)

result = func(lst)

with open('result35.json','w', encoding='utf-8') as f:
    f.write(json.dumps(result))

