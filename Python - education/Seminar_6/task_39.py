# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит 
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

from random import randint

# def createLst(n):
#     return list([randint(0, 9) for i in range(n)])

# n = int(input('Введите размеры массива #1: '))

# lst1 = createLst(n)
# print(lst1)
# lst2 = createLst(n)
# print(lst2)
# lst3 = []

# for i in lst1:
#     if i not in lst2:
#         lst3.append(i)
        
# print(lst3)

# def compare(sp1, sp2):
#     sp = []
#     for i in sp1:
#         if i not in sp2:
#             sp.append(i)
#     print(sp)


# try:
#     while True:
#         n = int(input('Введите количество 1: '))
#         lst1 = [randint(1, 9) for _ in range(n)]
#         print(lst1)
#         m = int(input('Введите количество 2: '))
#         lst2 = [randint(1, 9) for _ in range(m)]
#         print(lst2)
#         compare(lst1, lst2)
#         print()
# except:
#     print('Введены некорректные данные.\nВыход из программы.')
# exit()

# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве 
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

# def createLst(n):
#     return list([randint(0, 9) for i in range(n)])

# n = int(input('Введите размеры массива #1: '))

# lst1 = createLst(n)
# print(lst1)

# count = 0

# for i in range(1, n - 1):
#     if lst1[i] > lst1[i-1] and lst1[i] > lst1[i+1]:
#         count += 1
# print(count)

# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках

def pair(lst):
    count = 0
    myset = set(lst)
    for i in myset:
        x = lst.count(i)
        count += x // 2

    return count


n = int(input('Введите количество элементов списка: '))
lst1 = [randint(1, 9) for _ in range(n)]
print(lst1)
print(pair(lst1))


# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300 220 284
