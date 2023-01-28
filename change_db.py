import rw_mod


def create_data(file):
    list_all_person = read_file(file)
    id = len(list_all_person) + 1
    first_name = input('Введите фамилию: ')
    last_name = input('Введите имя: ')
    middle_name = input('Введите отчество: ')
    tel = input('Введите номер телефона: ')
    email = input('Введите Email: ')
    day_of_birth = input('Введите день рождения: ')
    course = input('Введите курс: ')
    group = input('Введите группу: ')
    teacher = input('Введите ФИО преподавателя: ')
    new_person = [id, first_name, last_name, middle_name, tel, email, day_of_birth, course, group, teacher]
    write_file(file, new_person)
    print('Данные успешно добавлены!')
    show_db('database.csv')