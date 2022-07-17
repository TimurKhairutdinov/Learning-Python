# Циклы


# def max_average(sp):
#     maxx = sp[0]
#     sr = 0
#     for i in range(len(sp)):
#         if sp[i] > maxx:
#             maxx = sp[i]
#         sr += sp[i]
#     sr = sr/len(sp)
#     rez = {}
#     rez['максимальный элемент'] = maxx
#     rez['среднее арифметическое'] = sr
#     k = (maxx, sr, rez)
#     return k


sp = [5, 11, 2, 3, 4, 8, 7, 55]

for i in sp:
    if i > 5:
        print(i)


