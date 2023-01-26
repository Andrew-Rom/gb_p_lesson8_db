from read_db import *
from change_db import *


def menu():
    while True:
        type_num = input("\n"
                         "*****************************************\n"
                         "* Добро пожаловать в базу данных школы  *\n"
                         "* английского языка Skyeng :            *\n"
                         "*****************************************\n"
                         "* 1 - Показать все записи               *\n"
                         "* 2 - Найти запись                      *\n"
                         "* 3 - Добавить запись                   *\n"
                         "* 4 - Редактировать запись              *\n"
                         "* 5 - Удалить запись                    *\n"
                         "* 6 - Экспорт/Импорт                    *\n"
                         "* 0 - Выход                             *\n"
                         "*****************************************\n"
                         "Ваш выбор: ")
        if type_num == '0':
            exit()
        elif type_num == '1':
            show_db()
        elif type_num == '2':
            search_in_db()
        elif type_num == '3':
            create_data()
        elif type_num == '4':
            change_data()
        elif type_num == '5':
            del_data()
        elif type_num == '6':
            check_input()
        elif type_num not in ['1', '2', '3', '4', '5', '6', '0']:
            print("Ошибка. Некорректный ввод.")
            continue
        else:
            break


def search_in_db():
    while True:
        type_num = input("\n"
                         "****************************************\n"
                         "* Поиск :                              *\n"
                         "****************************************\n"
                         "* 1 - Найти по ID                      *\n"
                         "* 2 - Найти по фамилии студента        *\n"
                         "* 3 - Показать ФИО всех студентов      *\n"
                         "* 4 - Показать студентов курса         *\n"
                         "* 5 - Показать студентов преподавателя *\n"
                         "* 6 - Показать студентов группы        *\n"
                         "* 0 - Предыдущее меню                  *\n"
                         "* 00 - Выход                           *\n"
                         "****************************************\n"
                         "Ваш выбор: ")
        if search_in_db not in ['1', '2', '3', '4', '5', '6', '0', '00']:
            print("Ошибка. Некорректный ввод.")
            continue
        elif search_in_db == '00':
            exit()
        elif search_in_db == '0':
            break
        else:
            request = entering_req(search_in_db)
            read_db.actions(search_in_db, request)
            exit()

def entering_req(op):
    while True:
        if op == 1:
            request = str(input("Введите ID студента: "))
            return request
        elif op == 2:
            request = str(input("Введите фамилию студента: "))
            return request
        elif op == 3:
            request = ''
            return request
        elif op == 4:
            request = str(input("Введите фамилию студента: "))
            return request        
        except:
            log.logging.error("Error")
            print("Error. Incorrect input.")
            return