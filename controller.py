import log
import user_interface as ui
import actions as act

def main_menu():
    while True:
        ui.show_main_menu()
        user_command = input('Пожалуйста, введите цифру, соответствующую пункту меню: ')
        if user_command == '0':
            log.logging.info('Stop program')
            ui.show_exit_message()
            exit()
        elif user_command == '1':
            pass
        elif user_command == '2':
            log.logging.error('Selected searching block')
            act.searching()
        elif user_command == '3':
            pass
        elif user_command == '4':
            pass
        elif user_command == '5':
            pass
        elif user_command not in ['0', '1', '2', '3', '4', '5']:
            log.logging.error('Incorrect selection')
            ui.show_error_menu()
            continue
        else:
            break

