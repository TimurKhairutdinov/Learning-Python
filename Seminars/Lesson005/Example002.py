# 33. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
    
#     *Пример:* 
    
#     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint


def GenerateTerms(coef: int, pow: int) -> str:
    if pow == 0:
        return f"{coef}"
    elif pow == 1:
        return f"{coef}*x"
    else:
        return f"{coef}*x^{pow}"


def Fun(k):
    coefficients = [randint(0, 100) for _ in range(k+1)]
    terms = [GenerateTerms(c, p)
             for (p, c) in enumerate(coefficients) if c != 0]
    return " + ".join(terms[::-1]) + " = 0"


try:
    k = int(input("Введите степень многочлена (натуральное число): "))
    if k <= 0:
        raise
except:
    print("Нужно было ввести натуральное число.")
else:
    result = Fun(k)
    print(result)
    with open("002.txt", "w") as f:
        f.write(result)
