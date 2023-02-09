# #посчитать сумму всех чисел от 1 до N, N вводит пользователь

# def summa(n):
#     sum=0
#     for i in range(n+1):
#        sum+=i
#     return sum

# def summa2(n):
#     sum=0
#     while True:
#        if n==0: 
#           break
#        sum+=n
#        n-=1
#     return sum

# def summa_rec(n):
#     if n==0: 
#         return 0
#     return n + summa_rec(n-1)

# # 5 + (4 + (3 + (2 + (1 + 0 ))))

# N = int(input("Введите целое число "))
# # sum  = 0
# # for i in range(N+1):
# #     sum+=i
# # print(sum)
# print(summa(N))
# print(summa2(N))
# print(summa_rec(N))

# n = int(input("Введите число: "))


# def fib_find(n):
#     if n == 0 or n==1:
#         return 1
#     else:
#         print([i for i in (0, n)])
#         return fib_find(n - 1) + fib_find(n - 2)


# num = fib_find(n)
# print(num)

# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое 
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

n = int(input("Введите число "))

def nat_num (n,m):
    if m == 1:
        return True
    elif n%m==0:
        return False
    else:
        return True and nat_num(n,m-1)
                
    
print("\n", nat_num(n,n-1), "\n", "\n")

# Задача №37. Решение в группах
# 15 минут
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

n = int(input('Введите N: '))

def addWord(ind, str):
    if (ind >= n):
        return str
    str += input(f'Введите {ind+1}-ый символ: ')
    return addWord(ind +1, str)

def revertStr(ind, inputStr, resultStr):
    if (ind < 0):
        return resultStr
    resultStr += inputStr[ind]
    return revertStr(ind -1, inputStr, resultStr)

inputStr = addWord(0, "")
torevertStr = revertStr(len(inputStr) -1, inputStr, "")
print(inputStr)
print(torevertStr)