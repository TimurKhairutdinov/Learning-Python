# Анонимные функции, lambda
# Функция как переменная.

def f(x):
    return x**2 
print(f(2)) # 4
print(type(f)) # <class 'function'>

g = f # Присвоение переменной g функции f

print(g(2)) # 4
print(type(g)) # <class 'function'>

# Применение 
# Передаём функцию, в качестве аргумента.
# Не результат функции передаётся, а именно логика.

def sum(x,y):
    return x+y

def mylt(x,y):
    return x*y

def calc(op, a, b):
    return op(a,b)

print(calc(sum, 4, 6)) # 10
print(calc(mylt, 2, 8)) # 16

e = sum 
s = mylt

print(calc(e, 7, 4)) # 11
print(calc(s, 8, 3)) # 24
# *-------------------------------------------------------*

# А теперь lambda!
# Anonymous!

# Переменной присваивается функция lambda
sum2 = lambda i, j: i+j

# Логика sum2 будет такой же как и у функции sum

print(type(sum2)) # <class 'function'>  

print(calc(sum2, 6, 2)) # 8
 
# Далее, мы можем пропустить присваивание функции отдельной переменной
# И передевать аргументом сразу lambda

print(calc(lambda arg1, arg2: arg1+arg2, 5529, 2955)) # 8484
print(calc(lambda arg1, arg2: arg1*arg2, 5529, 2955)) # 16338195 
# Wow!
# *-------------------------------------------------------*
