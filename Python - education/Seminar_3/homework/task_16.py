# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих 
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X

from random import randint

n = int(input('Введите размер массива: '))
lst = [randint(0, n) for i in range(n)]
print(lst)

a = int(input('Какое число нужно найти: '))

count = 0 

for i in lst:
    if i == a:
        count += 1

print(count)