def data_input():
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding='utf-8') as f:
        f.write(f'{contact}\n\n')
              
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