# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# 1
text = 'Текст – это несабвколько несабвколько предабвложений, абв 2 связанабвных связанных между собой . "абв"'
def del_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    print(text)
    return " ".join(text)


del_words(text)
print(del_words(text))

# 2
txt = 'Текст – это несабвколько несабвколько предабвложений, абв 2 связанабвных связанных между собой . "абв"'
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')

