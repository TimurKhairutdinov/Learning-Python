import json


def menu_user():
    print('Телефонный справочник.')
    print((\
            'Для работы, введите номер пункта меню.\n'
            '1. Добавить. \n'
            '2. Поиск. \n'
            '3. Изменить. \n'
            '4. Показать список контактов.\n'))
    choice = input('>> ')
    match choice:
        case '1': add_contact()
            # case '2':
            # case '3':
        case '4': view_contacts()
                

def menu_admin():
    print('Введите пароль: ')
    # 
    #
    #
            
def vvod():
    name = input('Введите Имя Фамилию>> ')
    number = input('Введите номер телефона: >> ')
    number_sec = input('Введите доп. номер телефона: >> ')
    comment = input('Введите комментарий: >> ')
    return {'name': name, 'number': number, 'number_sec': number_sec, 'comment': comment}



def add_contact():
    data = vvod()
    
    book = load_data_json()
    
    book[f'{data.get("number")}'] = data
    
    save_data_json(book)


def view_contacts():
    book = load_data_json()
    for contact in book:
        print(f'{contact.get("name")}: Num: {contact.get("number")}')
        


def save_data_json(arg):
    with open('book.json', 'w', encoding='utf-8') as telephon_book:
        telephon_book.write(json.dumps(arg, ensure_ascii=False))



def load_data_json():
    with open('book.json', 'r', encoding='utf-8') as telephon_book:
        data_from_telephon_book = json.load(telephon_book)
        return data_from_telephon_book
