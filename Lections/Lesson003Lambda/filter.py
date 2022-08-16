# Функция filter
# Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта и 
# возвращает итератор с теми объектами, для которых функция вернула True.
# f(x) => x - чётное
# filter(f, [1,2,3,4,5]) => [2,4]
# Нельзя пройтись дважды
# *-------------------------------------------------*
def where(f, lst):
    return [x for x in lst if f(x)]
# *-------------------------------------------------*
data = [i for i in range(1,11)]

res = filter(lambda x: x%2==0, data)

for i in res:
    print(i, end = ' ') # 2 4 6 8 10 
    
print(res) # <filter object at 0x000001FFEE767DF0>
print(type(res)) # <class 'filter'>

res = list(filter(lambda x: x%2==0, data))

print(res) # [2, 4, 6, 8, 10]
print(type(res)) # <class 'list'>

# python style use "not"

res = list(filter(lambda x: not x%2, data))
print(res) # [2, 4, 6, 8, 10]

res = list(filter(lambda x: x%2, data))
print(res) # [1, 3, 5, 7, 9] 
# *-------------------------------------------------*

