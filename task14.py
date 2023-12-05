# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
# 10 -> 1 2 4 8

# number = int(input('Enter number N: '))
number = 3
power = 0
while 2 ** power < number:
    print(2 ** power)
    power += 1

# k = 0
# while 2**k <= number:
#     print(2**k)
#     k += 1
