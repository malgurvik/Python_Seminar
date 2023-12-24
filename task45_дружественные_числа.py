# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 10^5. Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:
# 300
# Вывод:
# 220 284

k = 100000

# # -------------------------------------------------------------
# def divider(num):
#     my_div = 0
#     for i in range(1, num // 2 + 1):
#         if num % i == 0:
#             my_div += i
#     return my_div
#
#
# def frendly_num(a):
#     lst = []
#     for i in range(1, a + 1):
#         if i not in lst:
#             some = divider(i)
#             if divider(some) == i and i < some:
#                 lst.append((some, i))
#     return lst
#
# print(frendly_num(k))

# -------------------------------------------------------------
def sum_dividers(number: int):
    dividers = set()
    dividers.add(1)
    for i in range(2, int(number ** 0.5) + 1):
        if not number % i:
            dividers.add(i)
            dividers.add(number // i)

    return sum(dividers)


# def find_friendly(max_number: int):
#     for i in range(1, max_number + 1):
#         var = sum_dividers(i)
#         if var <= max_number:
#             if sum_dividers(var) == i:
#                 if i < var:
#                     print(i, var)

def frendly_num(a):
    lst = []
    for i in range(1, a + 1):
        if i not in lst:
            some = sum_dividers(i)
            if sum_dividers(some) == i and i < some:
                lst.append((some, i))
    return lst
# find_friendly(k)
print(frendly_num(k))
#
# # -------------------------------------------------------------
# def sum_of_divisors(num: int) -> int:
#     summ = {1}
#     for div in range(2, int(num ** 0.5) + 1):
#         if not num % div:
#             summ.add(div)
#             summ.add(num // div)
#     return sum(summ)
#
# friendly_dict = {i: sum_of_divisors(i) for i in range(1, 1000000)}
#
# for number, summ in friendly_dict.items():
#     if number == friendly_dict.get(summ) and number < summ:
#         print(number, summ)