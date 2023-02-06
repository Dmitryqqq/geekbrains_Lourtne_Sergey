# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# str = 'a a a b c a a d c d d'
# lst = str.split()

# print(lst)

# count = 0
# temp = lst[0]

# for i in range(1, len(lst)):
#     if len(lst[i]) == 1:
#         for v in range(i, len(lst)):
#             if temp == lst[v]:
#                 count += 1
#                 lst[v] += f'_{count}'
#         temp = lst[i]
#         count = 0

# print(lst)

# Задача №27. Общее обсуждение
# Пользователь вводит текст(строка). Словом считается 
# последовательность непробельных символов идущих 
# подряд, слова разделены одним или большим числом 
# пробелов или символами конца строки.Определите, 
# сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore;The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore,I'm sure that the shells are sea
# shore shells.
# Output: 19

# str = """She sells sea shells on the sea shore The shellsthat she sells are sea shells 
# I'm sure.So if she sells sea 
# shells on the sea shore I'm sure that the shells are sea
# shore shells"""

# znaki = ['.', ',',';']

# for z in znaki:
#     str = str.replace(z, ' ')

# print(str)

# lst = set(str.lower().split()) 

# print(len(lst))

# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит 
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не 
# такими смышлеными. Никто из ребят не смог до 
# конца сделать это задание. Они решили так: у кого 
# будет меньше ошибок в коде, тот и выиграл спор. За 
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих 
# слайдах
