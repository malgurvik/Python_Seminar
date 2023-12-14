# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

text = ('She sells sea shells on the sea shore The shells that she '
        'sells are sea shells I\'m sure. So if she sells sea shells on '
        'the sea shore I\'m sure that the shells are sea shore shells')
lst_text = text.lower().replace('.', '').split()
print(lst_text)
lst = set(lst_text)
for word in lst_text:
    if word not in lst_text:
        lst.add(word)
print(len(lst))
# print(len(lst_text))

# k = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea \
#     shells on the sea shore I'm sure that the shells are sea shore shells".lower().split()
# k = set(k)
# print(len(k))