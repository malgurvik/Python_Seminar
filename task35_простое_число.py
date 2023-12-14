# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes



def prime_number(num):
    if num <= 1:
        return 'no'
    elif num > 1:
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                return 'no'
    return 'yes'


num = int(input('Введите число: '))
print(prime_number(num))

# def prime_number(number):
#     if number in (1, 2):
#         return True
#     if not number % 2:
#         return False
#     for i in range(3, int(number ** 0.5), 2):
#         if not number % i:
#             return False
#     return True
#
# print(prime_number(int(input("Enter a number: "))))
