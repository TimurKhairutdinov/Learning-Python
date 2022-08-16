# Функция enumerate
# Функция enumerate() применяется к итерируемому объекту 
# и возвращает новый итератор с кортежами из индекса и элементов входных данных.

# enumerate(['Казань', 'Смоленск', 'Новгород', 'Москва'])
# result [(0,'Казань'), (1,'Смоленск'), (2,'Новгород'), (3, 'Мосвка')]
# Нельзя пройтись дважды

lst = ['Казань', 'Смоленск', 'Новгород', 'Москва']

data = enumerate(lst)

print(data) # <enumerate object at 0x000002B4325E34C0>
print(type(data)) # <class 'enumerate'>

data = list(enumerate(lst)) 

print(data) # [(0, 'Казань'), (1, 'Смоленск'), (2, 'Новгород'), (3, 'Москва')] 
print(type(data)) # <class 'list'>
 
 
workers = ['worker1', 'worker2', 'worker3', 'worker4', 'worker5']

print(list(enumerate(workers))) # [(0, 'worker1'), (1, 'worker2'), (2, 'worker3'), (3, 'worker4'), (4, 'worker5')]

job_title = ['web-dev', 'back-dev', 'front-dev', 'mobile-dev']

print(list(enumerate(job_title))) # [(0, 'web-dev'), (1, 'back-dev'), (2, 'front-dev'), (3, 'mobile-dev')]