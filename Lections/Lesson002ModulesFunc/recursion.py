# Рекурсия

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


list = []

for i in range(1, 33):
    list.append(fib(i))

print(list)
