# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Ввод:
#     orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
#     print(*find_farthest_orbit(orbits))
# Вывод:
#     2.5 10
from random import uniform

# def find_farthest_orbit(orbits):
#     # for i in orbits:
#     #     print(i[0] != i[1])
#     square_orbits = [(i[0] != i[1]) * i[0] * i[1] for i in orbits]
#     return orbits[square_orbits.index(max(square_orbits))]

# def find_farthest_orbit(lst):
#     lst1 = list(filter(lambda a: a[0] != a[1], lst))
#     max_orbit=0
#     max_ind=0
#     for i, item in enumerate(lst1):
#         a, b = item
#         if a * b > max_orbit:
#             max_orbit = a*b
#             max_ind = i
#     return lst1[max_ind]

# print(orbits := [(round(uniform(1, 15), 1), round(uniform(1, 15), 1)) for _ in range(6)])
print(orbits := [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)])
print(orbits := list(filter(lambda x: x[0] != x[1], orbits)))
print(max(orbits, key=lambda x: x[0] * x[1]))

# print(*find_farthest_orbit(orbits))
