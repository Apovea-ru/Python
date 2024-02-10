'''Создать телефонный справочник с возможностью импорта и экспорта 
данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные,
которые должны находиться в файле.
Программа должна выводить данные
Программа должна сохранять данные в текстовом файле
Пользователь может ввести одну из характеристик для поиска определенной
записи(Например имя или фамилию человека)
Использование функций. Ваша программа не должна быть линейной'''
from logging import *
from check import *
from ui import *

# def input_surname():
#     return input('Введите фамилию: ').title()

# def input_name():
#     return input('Введите имя: ').title()

# def input_patronymic():
#     return input('Введите отчество: ').title()

# def input_phone():
#     return input('Введите номер телефона: ')

# def input_address():
#     return input('Введите адрес (город): ').title()

# def create_contact():
#     surname = input_surname()
#     name = input_name()
#     patronymic = input_patronymic()
#     phone = input_phone()
#     address = input_address()
#     return f'{surname} {name} {patronymic} {phone}\n{address}'

# def data_input():
#     contact = create_contact()
#     with open('phonebook.txt', 'a', encoding='utf-8') as f:
#         f.write(f'{contact}\n\n')

# def read_file():
#     with open('phonebook.txt', 'r', encoding='utf-8') as f:
#         return f.read()

# def print_data():
#     print(read_file())


# def search_contact():
#     print(
#     'Варианты поиска:\n'\
#     '1 - по фамилии\n'\
#     '2 - по имени\n'\
#     '3 - по отчеству\n'\
#     '4 - по телефону\n'\
#     '5 - по адресу(городу)'
#     )
#     var = input('Выберите необходимый вариант: ')
#     while var not in ('1', '2', '3', '4', '5'):
#         print('Некорректный ввод данных!')
#         var = input('Выберите необходимый вариант: ')
#         print()
#     i_var = int(var) - 1

#     find = input('Введите данные для поиска: ').title()
#     print()
#     contacts = read_file()
#     contacts_list = contacts.strip().split('\n\n')
#     for contact_str in contacts_list:
#         contact_lst = contact_str.replace('\n', ' ').split()
#     # print(contact_lst)
#         if find in contact_lst[i_var]:
#             print(contact_str)
#             print()



# def interface():
#     with open("phonebook.txt", "a", encoding='utf-8'):
#         pass
#     choice = ''
#     print(
#         "Варианты действия: \n" \
#         "1 - Ввод данных контакта \n" \
#         "2 - Вывести данные на экран \n" \
#         "3 - Поиск контакта \n" \
#         "4 - Выход"
#         )
#     print()
#     choice = input("Выберите номер действия: ")
#     print()
#     while choice not in ('1', '2', '3', '4'):
#         print("Некорректный ввод данных!")
#         choice = input("Выберите номер действия: ")
#         print()
#     match choice:
#         case '1':
#             data_input()
#         case '2':
#             print_data()
#         case '3':
#             search_contact()
#         case '4':
#             print('Всего доброго!')

if __name__ == '__main__':
    interface()