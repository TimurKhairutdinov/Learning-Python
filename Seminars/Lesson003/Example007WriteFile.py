import json

def WriteJSON(file_name):
    with open('{file_name}', 'r', encoding='utf-8') as fn:
        file = json.load(fn)
    print('Файл загружен')