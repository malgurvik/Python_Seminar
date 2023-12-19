# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# Вывод:
#  3 3 2 12
# (каждое число вводится с новой строки)

import random


# lst_1 = [3, 1, 3, 4, 2, 4, 12]
# lst_2 =[4, 15, 43, 1, 15, 1]
n = int(input('Введите количество элементов в 1 массиве: '))
m = int(input('Введите количество элементов в 2 массиве: '))
lst_1 = []
lst_2 = []
for i in range(n):
    lst_1.append(random.randint(0, 50))
print(lst_1)
for i in range(m):
    lst_2.append(random.randint(0, 50))
print(lst_2)
result_lst = []
set1 = set(lst_2)
for item in lst_1:
    if item not in set1:
        result_lst.append(item)
print(result_lst)

# data = [i for i in lst_1 if i not in lst_2]

# change = set(lst_1).difference(lst_2)
#
# for i in lst_1:
#     if i in change:
#         print(i, end= ' ')