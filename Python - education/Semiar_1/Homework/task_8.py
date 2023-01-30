# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать 
# один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input('Введите кол-во долек по вертикали: '))
m = int(input('Введите кол-во долек по горизотали: '))
k = int(input('Введите кол-во долек которые нужно отламать: '))

if (k % n == 0 or k % m == 0) and k < n * m:
    print(f'Можно отломить на {k} долек')
else:
    print('Нельзя отломить на столько долек :(')