# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6


list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
lst = set(list_1)
for i in list_1:
    if i not in list_1:
        lst.append(i)
print(len(lst))
