# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.

n = int(input('Введите чётное число: '))

m = 1

if n % 2 == 0:
    while m * 2 <= n:
        m *= 2
        print(m)
else:
    print('Число должно быть чётным!')