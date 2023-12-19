# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:
# 1 2 3 2 3
# Вывод:
# 2

# lst = [1, 2, 3, 2, 3]
import random

# n = int(input('Введите количество элементов списка: '))
lst = [random.randint(0, 5) for i in range(int(input('Введите количество элементов списка: ')))]
print(lst)

result = []
for i in range(0, len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j] and not (lst[i] in result):
            result.append(lst[i])
print(len(result))
print(result)

result = 0
for item in set(lst):
    result += lst.count(item) // 2
print(result)

var = list(lst.count(i) // 2 for i in set(lst))
print(sum(var))
