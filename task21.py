# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

list_dicts = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
              {"VIII": "S007"}]
unique_values = set()
for dicts in list_dicts:  # проходим по спискам можества
    for value in dicts.values():  # проходим по значениям списка
        unique_values.add(value)
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
print(unique_values)

# data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#         {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII":"S007 "}]
# result = set()
# for i in data:
#     result.add(list(i.values())[0])
# print(result)
