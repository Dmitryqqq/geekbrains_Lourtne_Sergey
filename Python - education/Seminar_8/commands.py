import globals as g
import json

g.input_str = ''

def help_output(help_dict):
    for k, v in help_dict.items():
        print('{0:8s}:{1}'.format(k, v))

def quit_mess():
    print('Бот завершил свою работу!')
    print('До новых встреч в эфире!')
    with open('phones.json', 'w') as f:
        json.dump(g.data, f, indent=2)
    exit()

def add(data_list):
    input_dict = {
        'Фамилия:': 'Введите фамилию: ',
        'Имя:': 'Введите имя: ',
        'Отчество:': 'Введите отчество: ',
        'Телефоны:': 'Введите телефоны: ',
    }

    new_dict = {
        'Фамилия:': '',
        'Имя:': '',
        'Отчество:': '',
        'Телефоны:': {
            'моб': '',
            'раб': '',
        },
    }

    phone_dict = {
        'моб': 'Введите мобильный телефон: ',
        'раб': 'Введите рабочий телефон: ',
    }

    for k,v in input_dict.items():
        if not k == 'Телефоны:':
            text_input = input(input_dict[k])
            new_dict[k] = text_input
        else:
            print(input_dict[k])
            for j,s in phone_dict.items():
                    text_input = input(phone_dict[j])
                    new_dict[k][j] = text_input


        print(new_dict)