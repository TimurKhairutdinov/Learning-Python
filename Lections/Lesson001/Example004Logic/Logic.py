# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

a = 1 > 5
print(a)

b = 2 < 4 and 5 > 2
print(b)

c = 2 != 1 and 3 == 3
print(c)

s = 'Hello'
t = 'Hello'
print(s == t)

l = [1, 2]
l2 = [1, 2]
print(l == l2)

# неравенства
n = 1 < 2 < 4
print(n)

func = 1
T = 4
x = 2
print(func < T > (x))

# or, and
f = 1 > 2 or 4 < 6
g = 1 > 2 and 4 < 6
print(f)
print(g)

# in, not
list = [1, 2, 3, 4]
print(list)
print(5 in list)
print(not 5 in list)

is_odd = list[0] % 2 == 0
print(is_odd)

is_odd = not list[0] % 2
print(is_odd)
