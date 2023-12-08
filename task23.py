# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

import random

my_list = []
start_list = 0
end_list = 10
length = 5

for i in range(length):  # Используем range для итерации по длине

    my_list.append(random.randint(start_list, end_list))  # Добавляем случайное число в список
print(my_list)
count=0
for i in  range(len(my_list)-1):
    if my_list[i+1]>my_list[i]:
        count+=1

print(count)

# data = []
# start_data = 0
# end_data = 10
# length = 5
# count = 0
#
# for i in range(length):
#     random_number = random.randint(start_data, end_data)
#     data.append(random_number)
# print(data)
#
# for i in range(1, len(data)):
#     if data[i - 1] < data[i]:
#         count += 1
# print(count)
#
# lenlst = int(input("Введите длину списка: "))
# count = 0
# lst = []
#
# for i in range(lenlst):
#     lst.append(random.randint(1, 10))
#     if lst[i] > lst[i-1]:
#         count += 1
#
# print(lst)
# print(count)
