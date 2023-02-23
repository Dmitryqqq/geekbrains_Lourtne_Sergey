from random import *
import json

films=[]

def save():
    with open("Python - education/Seminar_7/films.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(films,ensure_ascii=False))
    print("Наша фильмотека была успешно сохранена в файле films.json")

def load():
    global films
    with open("Python - education/Seminar_7/films.json","r",encoding="utf-8") as fh:
        films=json.load(fh)
    print("Фильмотека была успешно загружена")   

try:
    load()
except:
    films.append('Матрица')
    films.append('Солярис')
    films.append('Властилин колец')
    films.append('Техасская резня бензопилой')
    films.append('Санта Барбара')


while True:
    command=input("Введите комманду: ")
    if command=="/start":
        print("Бот начал свою работу")
    elif command=="/stop":
        save()
        print("Файлс сохранён!")
        break
    elif command=="/all":
        print("Список всех фильмов: ")
        print(films)
    elif command =="/add":
        f=input("Введите название фильма: ")
        films.append(f)
        print("Фильм добавили в список!")
    elif command=="/help":
        print("Список комманд: /start - начать работу /stop - закончить работу /all - показать список всех фильмов /add - добавить фильм")
    elif command=="/delete":
        f=input("Введите название фильма, который нужно удалить ")
        try:
            films.remove(f)
            print("Фильм удалён!")
        except:
            print("Нет такого фильма(")
    elif command=="/random":
       print("Случайный фильм -" + choice(films) )
    elif command =="/save":
        save()
    elif command=="/load":
        load()
    else:
        print("Неверная комманда. Список актуальных комманд: /help")