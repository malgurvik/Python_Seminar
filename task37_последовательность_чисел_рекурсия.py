# Задача №37. Решение в группах
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def func(num):
#     number = input()
#     if num == 1:
#         return number
#     return func(num - 1) + ' ' + number

def func(num):
    if num == 0:
        return ''
    number = input()
    return func(num - 1) + ' ' + number

n = int(input('Введите число: '))
print(funk(n))