def input_surname():
    return input('Введите фамилию: ').title()

def input_name():
    return input('Введите имя: ').title()

def input_patronymic():
    return input('Введите отчество: ').title()

def input_phone():
    return input('Введите номер телефона: ')

def input_address():
    return input('Введите адрес (город): ').title()

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic} {phone}\n{address}'

def data_input():
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding='utf-8') as f:
        f.write(f'{contact}\n\n')

def read_file():
    with open('phonebook.txt', 'r', encoding='utf-8') as f:
        return f.read()

def print_data():
    read_file()
        
def copy_date():
    contacts = read_file()
    contacts_list = contacts.strip().split('\n\n')
    for contact in enumerate(contacts_list, 1):
        print(*contact)
    i = int(input('Выберите номер нужной строчки для копирования: ')) - 1
    for k in range(len(contacts_list)):
        if k == i:
            copydate = contacts_list[i]
    new_file = input('Назовите файл, куда надо копировать: ')
    with open (new_file, 'a', encoding='utf-8') as f:
        f.write(f'{copydate}\n\n')
        
            
    
    
def search_contact():
    print(
    'Варианты поиска:\n'\
    '1 - по фамилии\n'\
    '2 - по имени\n'\
    '3 - по отчеству\n'\
    '4 - по телефону\n'\
    '5 - по адресу(городу)'
    )
    var = input('Выберите необходимый вариант: ')
    while var not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод данных!')
        var = input('Выберите необходимый вариант: ')
        print()
    i_var = int(var) - 1

    find = input('Введите данные для поиска: ').title()
    print()
    contacts = read_file()
    contacts_list = contacts.strip().split('\n\n')
    for contact_str in contacts_list:
        contact_lst = contact_str.replace('\n', ' ').split()
        if find in contact_lst[i_var]:
            print(contact_str)
            print()



def interface():
    with open("phonebook.txt", "a", encoding='utf-8'):
        pass
    choice = ''
    print(
        "Варианты действия: \n" \
        "1 - Ввод данных контакта \n" \
        "2 - Вывести данные на экран \n" \
        "3 - Поиск контакта \n" \
        "4 - Скопировать нужные данные в новый файл \n"
        "5 - Выход"
        )
    print()
    choice = input("Выберите номер действия: ")
    print()
    while choice not in ('1', '2', '3', '4'):
        print("Некорректный ввод данных!")
        choice = input("Выберите номер действия: ")
        print()
    match choice:
        case '1':
            data_input()
        case '2':
            print_data()
        case '3':
            search_contact()
        case '4':
            copy_date()
        case '5':
            print('Всего доброго!')

if __name__ == '__main__':
    interface()