#
#
a = {}
a['Дима'] = 123456
a['Маша'] = 654321

print(a.keys())
print(a.values())
print()
print(a.items())
print()
print(a.get('Дима'))
print(a)
print()
print(a.fromkeys('123456',5))

a['Марина'] = 90
a['Дима'] = 123
a['Маша'] = 52
# a.pop
# a.popitem
# del a['Маша']
a.clear()
print(a)