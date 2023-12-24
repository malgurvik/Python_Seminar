# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод:
#     values = [0, 2, 10, 6]
#     if same_by(lambda x: x % 2, values):
#         print(‘same’)
#     else:
#         print(‘different’)
# Вывод:
#     same


# def same_by(characteristic, objects):
#     if len(objects) == 0:
#         return True
#     first_object = characteristic(objects[0])
#     for i in range(len(objects)):
#         if first_object != characteristic(objects[i]):
#             return False
#     return True

def same_by(characteristic, objects):
    return len(set(map(characteristic, values))) < 2

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
