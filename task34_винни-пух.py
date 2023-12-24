# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод:
# Парам пам-пам

# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'  # pass
# stroka = 'Пух'  # min word
# stroka = 'со-лнце-гре-ет ве-сной' #  no
stroka = 'за-гад-ка-ра-свет-ка-ра-газ-да-не-на-ма-ли-ва-ла'  # min word
# stroka = 'как ве-тер сме-ёт лис-ти' #  no
# stroka = 'мо-локо и мёд' #  pass
# stroka = 'по-русски говорят'  # yes

vowels = set('уеыаоэяию')


def vowel_count(string):
    string = list(string.lower().split())
    lst = []
    for i in range(len(string)):
        count = 0
        for letter in string[i]:
            if letter in vowels:
                count += 1
        lst.append(count)
    return lst


def rythm_check(list_):
    if len(list_) > 1:
        for i in range(len(list_) - 1):
            if list_[i] == list_[i + 1]:
                return 'Парам пам-пам'
            return 'Пам парам'
    else:
        return 'Количество фраз должно быть больше одной!'


print(rythm_check(vowel_count(stroka)))

#-------------------------------------------------------------------------------

phrases = stroka.split()
if len(phrases) < 2:
    print('Количество фраз должно быть больше одной!')
else:
    countVowels = []

for i in phrases:
    countVowels.append(len([x for x in i if x.lower() in vowels]))

if countVowels.count(countVowels[0]) == len(countVowels):
    print('Парам пам-пам')
else:
    print('Пам парам')
