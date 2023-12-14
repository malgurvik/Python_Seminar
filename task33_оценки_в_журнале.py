# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def assessment(lst: list):
    maximum = 0
    minimum = float('inf')
    for i in lst:
        if maximum < i:
            maximum = i
        if minimum > i:
            minimum = i
    print(maximum, minimum)
    for i in range(len(lst)):
        if lst[i] == maximum:
            lst[i] = minimum
    return lst


jurnal = [1, 3, 3, 3, 4]
print(assessment(jurnal))
