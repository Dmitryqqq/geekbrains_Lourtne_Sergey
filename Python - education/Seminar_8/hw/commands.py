import json
import globals as g

def save():
    with open("Python - education/Seminar_8/hw/phonebook.json","w",encoding="utf-8") as fb:
        fb.write(json.dumps(g.phonebook, ensure_ascii=False))
    print("Телефонный справочник был успешно сохранен в файле phonebook.json")

def load():
    with open("Python - education/Seminar_8/hw/phonebook.json","r",encoding="utf-8") as fb:
        g.phonebook = json.load(fb)
    print("Телефонный справочник был успешно загружен.")   

def clear():
    g.phonebook.clear()
    print("Телефонный справочник был успешно очищен.\nНе забудьте сохранить изменения!\n")

def add():
    print('''
    Для того, чтобы добавить человека в телефонную книгу следуйте инструкциям ниже.
    Ecли какой-то параметр остутствует введите -\n''')
    f = input("Введите фамилию: ")
    name = input("Введите имя: ")
    secondName = input("Введите отчество: ")
    number = input("Введите мобильный телефон: ")
    g.phonebook.append({
    'Фамилия:': f'{f}',
    'Имя:': f'{name}',
    'Отчество:': f'{secondName}',
    'Телефон:': f'{number}'
    })
    print("Абонент успешно добавлен в телефонный справочник!\n")

def all():
    if g.phonebook == []:
        print('Книга пуста!')
    else:
        count = 0
        for i in g.phonebook:
            count += 1
            print(f'\nАбонент №{count}')
            for key, value in i.items():
                print(f'{key} {value}')