import user_inerface
db_file_name = ''
db = []
global_id = 0


def users_check(arg):
    while arg.isdigit() != True:
        arg = input('Пожалуйста, введите цифру, соответствующую пункту меню: ')
    return int(arg)


def searching():
    users_check()
    show_search_menu()
    if n == 1:
        search = input('Пожалуйста, введите id студента: ')
        print(students_info(id=search))
    elif n == 2:
        input('Пожалуйста, введите фамилию студента: ')
        print(students_info(surname=search))
    elif n == 3:
        print(students_info())
    elif n == 4:
        input('Пожалуйста, введите наименование курса: ')
        print(students_info(course=search))
    elif n == 5:
        input('Пожалуйста, введите фамилию преподавателя: ')
        print(students_info(mentor=search))
    elif n == 6:
        input('Пожалуйста, введите группу: ')
        print(students_info(group=search))
    elif n == 0:
        print('Возврат в предыдущее меню')
        show_main_menu()
    elif n == 00:
        print('Конец работы программы')
        exit()
    else:
        print('Пожалуйста, введите цифру, соответствующую пункту меню: ')


def students_info(id='', surname='', name='', patronymic='', group='', mentor=''):
    global global_id
    global db
    global db_file_name
    result = []
    for row in db:
        if (id != '' and row[0] != id):
            continue
        if (surname != '' and row[1] != surname.title()):
            continue
        if (name != '' and row[2] != name.title()):
            continue
        if (patronymic != '' and row[3] != patronymic.title()):
            continue
        if (group != '' and row[4] != group):
            continue
        if (mentor != '' and row[5] != mentor.title()):
            continue
        result.append(row)
    if len(result) == 0:
        return f'Студенты не найдены'
    else:
        return result
