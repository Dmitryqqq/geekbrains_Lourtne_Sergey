# lst = [i for i in range(100)]   

# def decision(lst):
#     for i in lst:
#         if i % 2 == 0 and i > 0:
#             j = i * i
#             if i * i < 100:
#                 print(f'({i}, {j})')

# print(decision(lst))


# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.


# values = [1, 23, 42, 'asdfg'] #[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# trasformation = lambda x: x
# transformed_values = list(map(trasformation, values))
# transformed_values[0] += 1

# res = list(filter(lambda x: x[0] == x[1], zip(values, transformed_values)))
# print('ok') if res == transformed_values else print('fail')
# print(values)
# print(transformed_values)
# print(res)

# Планеты вращаются вокруг звезд по эллиптическим орбитам. 
# Назовем самой далекой планетой ту, орбита которой имеет 
# самую большую площадь. Напишите функцию 
# find_farthest_orbit(list_of_orbits), которая среди списка орбит 
# планет найдет ту, по которой вращается самая далекая 
# планета. Круговые орбиты не учитывайте: вы знаете, что у 
# вашей звезды таких планет нет, зато искусственные спутники 
# были были запущены на круговые орбиты. Результатом 
# функции должен быть кортеж, содержащий длины полуосей 
# эллипса орбиты самой далекой планеты. Каждая орбита 
# представляет из себя кортеж из пары чисел - полуосей ее 
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, 
# где a и b - длины полуосей эллипса. При решении задачи 
# используйте списочные выражения. Подсказка: проще всего 
# будет найти эллипс в два шага: сначала вычислить самую 
# большую площадь эллипса, а затем найти и сам эллипс, 
# имеющий такую площадь. Гарантируется, что самая далекая 
# планета ровно одна

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# # def orbita(array):
# #     maxi_orbit = 0
# #     for i in range(len(array)):
# #         for j in range(0,2):
# #             if j == 0:
# #                 x = array[i][j]
# #             y = array[i][j]
# #         if x != y:
# #             S = 3.14 * x * y
# #         if maxi_orbit < S:
# #             maxi_orbit = S 
# #             orb = i  
# #     return orb
# # print(orbits[orbita(orbits)])

# # def find_farthest_orbit(list_of_orbits):
# #     maxi_orbit = 0

# #     # s = list(filter(lambda x, у : if , ))

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# def orbita(array):
#     maxi_orbit = 0
#     for i in range(len(array)):
#         for j in range(0,2):
#             if j == 0:
#                 x = array[i][j]
#             y = array[i][j]
#         if x != y:
#             S = lambda x,y: 3.14 * x * y
#             if maxi_orbit < S(x,y):
#                 maxi_orbit = S(x,y) 
#                 orb = i  
#     return orb
# print(orbits[orbita(orbits)])


# Напишите функцию same_by(characteristic, objects), которая 
# проверяет, все ли объекты имеют одинаковое значение 
# некоторой характеристики, и возвращают True, если это так. 
# Если значение характеристики для разных объектов 
# отличается - то False. Для пустого набора объектов, функция 
# должна возвращать True. Аргумент characteristic - это 
# функция, которая принимает объект и вычисляет его 
# характеристику.

# values = [0, 2, 11, 6]

# def same_by(characteristic, objects):
#     # return len(set(map(characteristic, objects)))
#     s = set([characteristic(x) for x in objects])
#     if len(s) == 1:
#         return True 
#     else:
#         return False

# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')

line = "если-я-чушу в-затылке-не-беда"
lines = line.split()
 
print(lines)