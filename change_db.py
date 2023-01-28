import rw_mod as db


def create_data():
    db.read_file()
    id = db.last_id + 1
    first_name = input('Введите фамилию: ')
    last_name = input('Введите имя: ')
    middle_name = input('Введите отчество: ')
    tel = input('Введите номер телефона: ')
    email = input('Введите Email: ')
    day_of_birth = input('Введите день рождения: ')
    course = input('Введите курс: ')
    group = input('Введите группу: ')
    teacher = input('Введите ФИО преподавателя: ')
    new_person = [str(id), first_name, last_name, middle_name, tel, email, day_of_birth, course, group, teacher]
    db.add_data(new_person)
    print('Данные успешно добавлены!')
    input('Для продолжения нажмите кнопку ввода...')
