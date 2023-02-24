from random import *
import json
import commands as cmds
import globals as g

g.phonebook = []

try:
    cmds.load()
    print('Добро пожаловать в телефонный справочник!\nСписок всех команд: /help')
except:
    print('Добро пожаловать в телефонный справочник!\nСписок всех команд: /help')
    with open("Python - education/Seminar_8/hw/phonebook.json","w",encoding="utf-8") as fb:
        fb.write(json.dumps(g.phonebook, ensure_ascii=False))

while True:
    command=input("Введите комманду: ")
    if command=="/stop":
        cmds.save()
        print("До следующей встречи!")
        break
    elif command=="/all":
        cmds.all()      
    elif command =="/add":
        cmds.add()
    elif command=="/delete":
        f = int(input("Введите номер абонента, которого нужно удалить: "))
        try:
            g.phonebook.pop(f-1)
            print(f"Абонент №{f} удалён!")
        except:
                print("Нет такого Абонента(")
    elif command=="/random":
       print("Случайный фильм -" + choice(g.phonebook) )
    elif command =="/save":
        cmds.save()
    elif command=="/load":
        cmds.load()
    elif command=="/clear":
        cmds.clear()
    elif command=="/red":
        cmds.red()
    elif command=="/show":
        cmds.show()
    elif command=="/help":
        print('''Список комманд:\n
        /stop - закончить работу;
        /all - показать список всех абонентов;
        /add - добавить абонента;
        /delete - удалить абонента;
        /save - сохранить измения в файле;
        /load - загрузить данные из файла;
        /clear - очистить текущий справочник;\n''')
    else:
        print("Неверная комманда. Список актуальных комманд: /help")