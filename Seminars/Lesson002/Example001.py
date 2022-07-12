# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def test(x, y, z):
    if not(x or y or z) == ((not(x)) and (not(y)) and (not(z))):
        return 1
    else:
        return 0


result = ''
for i in 1, 0:
    for j in 1, 0:
        for k in 1, 0:
            result += f'{i, j, k} = {test(i, j, k)} \n'
print(result)
