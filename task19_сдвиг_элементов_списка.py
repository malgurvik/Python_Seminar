# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# list_1 = [1, 2, 3, 4, 5]
# k = 3
# list_2 = list_1[k:] + list_1[:k]
# print(list_2)

lst = [1, 2, 3, 4, 5]
lst_shifted = []
shift = 1
for i in range(len(lst)):
    lst_shifted.append(lst[(i + shift) % len(lst)])
    print(lst_shifted)
