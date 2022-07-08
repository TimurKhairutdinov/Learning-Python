# Строки

text = '(C) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.'

print(len(text))  # 70
print('Microsoft' in text)  # True
print(text.isdigit())   # False
print(text.islower())   # False
print(text.replace('й', 'i'))

# Срезы

print(text[1])  # C
print(text[30])  # r
print(text[len(text)-1])  # Последний символ .
print(text[-8])  # a Если первый символ индекс 0, то индекс последнего -1.
# [:] - По сути это отрезок строки, где [начальный индекс : конечный индекс]
# По умолчанию заполнено [0:len - 1]
print(text[:])  # print(text)
print(text[6:25]) # рпорация Майкрософт
print(text[5:55]) # орпорация Майкрософт (Microsoft Corporation). Все
print(text[5:-15]) # орпорация Майкрософт (Microsoft Corporation). Все
# [0:55:5] - где 5 это интервал, то есть каждый 5 символ
print(text[:55:5])

