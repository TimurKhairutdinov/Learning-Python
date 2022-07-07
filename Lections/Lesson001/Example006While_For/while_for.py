# while
# for

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
    print(inverted)
# while-else
else:
    print('Достаточно')
print(inverted)

n = 5
i = 0
while i <= n:
    print(i)
    i += 1

# for
list = [1,2,3,4,5]
for i in list:
    print(i**2)

r = range(0,10,2)
for i in r: 
    print(i)

for i in 'Hello world!':
    print(i)