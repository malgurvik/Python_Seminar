# Задача №49. Решение в группах
# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые
# должны находиться в файле.
#     1. Программа должна выводить данные
#     2. Программа должна сохранять данные в
#         текстовом файле
#     3. Пользователь может ввести одну из
#         характеристик для поиска определенной
#         записи(Например имя или фамилию
#         человека)
#     4. Использование функций. Ваша программа
#         не должна быть линейной.


def print_menu():
    print('1 - Создать контакт')
    print('2 - Найти контакт')
    print('3 - Показать все контакты')
    print('4 - Изменить контакт')
    print('5 - Удалить контакт')
    print('6 - Импорт/Экспорт контактов')
    print('7 - Выход')


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lst = sorted(list(map(lambda x: x.strip(), file.readlines())))
        dictionary = dict(enumerate(lst, 1))
    return dictionary


def close_file(dictionary, file_name):
    lst = [value.split(':') for value in dictionary.values()]
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in lst:
            file.write(':'.join(i) + '\n')
    print('Изменения сохранены')


def create_contact(file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        contacts = [input('Введите имя:'), input('Введите номер телефона:'), input('Введите комментарий:')]
        file.writelines(': '.join(contacts) + '\n')
    print('Контакт сохранен')
    print()


def find_contact(file_name):
    contacts = read_file(file_name)
    name = input('Введите имя: ')
    data = None
    for value in contacts.values():
        if name.lower() in value.lower():
            data = value
            print(data)
    return data


def show_all_contacts(file_name):
    contacts = read_file(file_name)
    for value in contacts.values():
        print(value, end='\n')


def change_contact(file_name):
    contacts = read_file(file_name)
    # print(contacts)
    name = input('Введите имя контакта который хотите изменить: ')
    count = 0
    id_ = None
    for key, value in contacts.items():
        if name.lower() in value.lower():
            count += 1
            id_ = key
            print(key, value, end='\n')
    if count > 1:
        key = int(input('Выберите ID контакта: '))
        data_ = list(contacts[key].split(': '))
        print('1 - Имя\n2 - Номер телефона\n3 - Комментарий\n4 - Весь контакт')
        action = int(input('Что хотите изменить? '))
        if action == 1:
            print(data_[0])
            data_[0] = input('Введите имя: ')
        elif action == 2:
            print(data_[1])
            data_[1] = input('Введите номер телефона: ')
        elif action == 3:
            print(data_[2])
            data_[2] = input('Введите комментарий: ')
        elif action == 4:
            data_ = [input('Введите имя: '),
                     input('Введите номер телефона: '),
                     input('Введите комментарий: ')]
        contacts[key] = ': '.join(data_)
    elif count == 1:
        data_ = list(contacts[id_].split(': '))
        print('1 - Имя\n2 - Номер телефона\n3 - Комментарий\n4 - Весь контакт')
        action = int(input('Что хотите изменить? '))
        if action == 1:
            print(data_[0])
            data_[0] = input('Введите имя: ')
        elif action == 2:
            print(data_[1])
            data_[1] = input('Введите номер телефона: ')
        elif action == 3:
            print(data_[2])
            data_[2] = input('Введите комментарий: ')
        elif action == 4:
            data_ = [input('Введите имя: '),
                     input('Введите номер телефона: '),
                     input('Введите комментарий: ')]
        contacts[id_] = ': '.join(data_)

    close_file(contacts, file_name)


def delete_contact(file_name):
    contacts = read_file(file_name)
    name = input('Введите имя контакта который хотите удалить: ')
    count = 0
    id_ = None
    for key, value in contacts.items():
        if name.lower() in value.lower():
            count += 1
            id_ = key
            print(key, value, end='\n')
    if count > 1:
        key = int(input('Выберите ID контакта: '))
        del contacts[key]

    elif count == 1:
        del contacts[id_]
    close_file(contacts, file_name)


def find_for_export(file_name, file_name2):
    contacts = read_file(file_name)
    name = input('Введите имя контакта который хотите копировать: ')
    count = 0
    id_ = None
    for key, value in contacts.items():
        if name.lower() in value.lower():
            count += 1
            id_ = key
            print(key, value, end='\n')
    if count > 1:
        key = int(input('Выберите ID контакта: '))
        data_ = list(contacts[key].split(': '))
        with open(file_name2, 'a', encoding='utf-8') as file:
            # contacts = [input('Введите имя:'), input('Введите номер телефона:'), input('Введите комментарий:')]
            file.writelines(': '.join(data_) + '\n')
        print('Контакт скопирован')
        # print()
    elif count == 1:
        data_ = list(contacts[id_].split(': '))
        with open(file_name2, 'a', encoding='utf-8') as file:
            # contacts = [input('Введите имя:'), input('Введите номер телефона:'), input('Введите комментарий:')]
            file.writelines(': '.join(data_) + '\n')
        print('Контакт скопирован')


def import_export_contacts(file_name, file_name2):
    print(file_name)
    print(file_name2)
    contacts_for_export = input('Выберите файл из которого экспортировать: ')
    contacts_for_import = input('Выберите куда импортировать: ')
    while True:
        print('1 - Скопировать все контакты')
        print('2 - Скопировать определенный контакт')
        print('3 - Выход')
        action = int(input('Что хотите выполнить? '))
        if action == 1:
            close_file(read_file(contacts_for_export), contacts_for_import)
        elif action == 2:
            find_for_export(contacts_for_export, contacts_for_import)
        elif action == 3:
            break


# file1 = 'test.txt'
# file2 = 'test2.txt'
# import_export_contacts(file1, file2)


def main(file_name, file_name2):
    while True:
        print_menu()
        action = int(input('Введите действие: '))
        if action == 1:
            create_contact(file_name)
        elif action == 2:
            find_contact(file_name)
        elif action == 3:
            show_all_contacts(file_name)
        elif action == 4:
            change_contact(file_name)
        elif action == 5:
            delete_contact(file_name)
        elif action == 6:
            import_export_contacts(file_name, file_name2)
        elif action == 7:
            break
    print('До свидания!')


file1 = 'phonebook.txt'
file2 = 'phonebook_copy.txt'
main(file1, file2)
