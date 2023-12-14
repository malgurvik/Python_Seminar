# Задача №13. Решение в группах
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

import random

# print(random.randint(-50,50))

days = int(input("Введите количество дней: "))
count = 0
tempmax = 0
#while days > 0:
for _ in range(days):
    daytemp = random.randint(-50, 50)
    print(daytemp, end=" ")
    #days -= 1
    if daytemp > 0:
        count += 1
        if tempmax < count:
            tempmax = count
    else:
        count = 0

print(f"\nСамая длинная оттепель, дней: {tempmax}")

# usernum = int(input("Please input your amount of days: "))
# sum_ = 0
# max_ = 0
#
# for _ in range(usernum):
#     daytemp = random.randint(-50, 50)
#     print(daytemp, end=' ')
#     if daytemp > 0:
#         sum_ += 1
#         if max_ < sum_:
#             max_ = sum_
#     else:
#         sum_ = 0
# print()
# print(f"Number >0 days: {max_}")

# temps = [random.randint(-50, 50) for i in range(int(input("Enter the amount of days: ")))]
# max, count = 0, 0
#
# for day in temps:
#     if day > 0:
#         count += 1
#     else:
#         if max < count:
#             max = count
#         count = 0
#
# if max < count:
#     max = count
# print(temps, '\n', max)