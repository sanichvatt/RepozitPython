# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
# для изменения и удаления данных




def write_person(second_name, first_name, phone):
    with open('directory.txt', 'a') as f:
        f.write(f'\n{second_name}, {first_name}, {phone}')

def write_data():
    second_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    write_person(second_name, first_name, phone)

write_data()

def find_person():
    second_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    data = open('directory.txt', 'r')
    for line in data:
        if second_name or first_name or phone:
            print(data.readline())
    data.close()

find_person()

def find_person_correct():
    second_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    data = open('directory.txt', 'r')
    for line in data:
        if second_name or first_name or phone:
            print(data.readline())
    data.close()

path = 'directory.txt'


def update_contact():
    search_name = input('Введите фамилию контакта, который хотите изменить: ')
    with open("directory.txt", "r") as f:
        lines = f.readlines()
    with open("directory.txt", "w") as f:
        for line in lines:
            contact = line.strip().split(', ')
            if search_name.lower() not in contact[0].lower():
                print('Контакт не найден.')
            else:    
                new_second_name = input('Введите новую фамилию: ')
                new_first_name = input('Введите новое имя: ')
                new_phone = input('Введите новый номер телефона: ')
                f.write(f'{new_second_name}, {new_first_name}, {new_phone}\n')
                print('Контакт успешно изменен!')                        
                f.write(line)




def delete_contact():
    search_name = input('Введите фамилию контакта, который хотите удалить: ')
    with open("directory.txt", "r") as f:
        lines = f.readlines()
    with open("directory.txt", "w") as f:
        contact_found = False
        for line in lines:
            contact = line.strip().split(', ')
            if search_name.title() not in contact[0].title():
                f.write(line)
            else:
                contact_found = True
        if contact_found:
            print('Контакт успешно удален!')
        else:
            print('Контакт не найден.')