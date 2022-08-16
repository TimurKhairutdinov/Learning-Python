# Функция zip
# Функция zip() применяется к набору итеруремых объектов и возвращает итератор с кортежами из элементов входных данных.
# Количество элементов в резултате равно минимальному количеству элементов входного набора
# zip ([1,2,3], ['o', 'd', 't'], ['f', 's', 'e'])
# result [(1, 'o', 'f'), (2, 'd', 's'), (3, 't', 'e')]
# Нельзя пройтись дважды

users = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6']

ids = [4, 5, 2, 7, 15]

data = zip(users, ids)

print(data) # <zip object at 0x000001967848D780>
print(type(data)) # <class 'zip'>

data = list(zip(users, ids))

print(data) # [('user1', 4), ('user2', 5), ('user3', 2), ('user4', 7), ('user5', 15)]
print(type(data)) # <class 'list'>
# Функция zip применяется по минимальному входящему набору,
# в данном случае users содержит 6 элементов, а ids только 5.
# Поэтому результатом работы zip, будет список из 5 кортежей соотвествующих минимальному размеру входных данных ids.

# Ещё пример.

workers = ['worker1', 'worker2', 'worker3', 'worker4', 'worker5']
job_title = ['web-dev', 'back-dev', 'front-dev', 'mobile-dev']
salary = [1200, 1300, 1100]

data = list(zip(workers, job_title, salary))

print(data) 
# [('worker1', 'web-dev', 1200), ('worker2', 'back-dev', 1300), ('worker3', 'front-dev', 1100)]
# Результат работы zip, список из 3 кортежей, так как минимальный размер входных данных 3 salary