# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

import random

watermelon = int(input("Введите количество арбузов: "))

watermelon_max, watermelon_min = 0, 100

for _ in range(watermelon):
    watermelon_weight = random.randint(1, 20)
    print(watermelon_weight, end=" ")
    if watermelon_max < watermelon_weight:
        watermelon_max = watermelon_weight
    if watermelon_min > watermelon_weight:
        watermelon_min = watermelon_weight

print(f"\nСамый лёгкий арбуз весит, кг: {watermelon_min}\nСамый тяжёлый арбуз весит, кг: {watermelon_max}")
