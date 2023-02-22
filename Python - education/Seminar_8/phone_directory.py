import commands as cmds
import globals as g
import json
g.data = []
g.temp_dict = {}

help_dict = {
    'h': 'Справка',
    'start': 'Начать работу',
    'Q': 'Завершить работу',
    'a': 'Добавить контакт',
    'd': 'Удалить контакт',
}

print('Добро пожаловать в телефонный справочник!')
while True:
    cmd = input('Введите комманду (> h - справка, > start - начало работы, > Q - завершить)\n> ')
    if not cmd == 'h' and not cmd == 'start':
        print('Введена неверная команда!')
        continue
    if cmd == 'h':
        cmds.help_output(help_dict)
    if cmd == 'start':
        print('Бот начал свою работу!')
        with open('phones.json', 'r') as f:
            g.data = json.load(f)
            print(g.data)
        break
    if cmd == 'Q':
        cmds.quit_mess()


while True:
    cmd = input('Введите комманду (> \'Q\' - завершить): \n> ')
    if cmd not in help_dict:
        print('Команды не существует!')
        continue
    if cmd == 'Q':
        cmds.quit_mess()
    if cmd == 'start':
        print('Бот уже трудится!')
    if cmd == 'h':
        cmds.help_output(help_dict)
    if cmd == 'a':
        cmds.add(g.data)