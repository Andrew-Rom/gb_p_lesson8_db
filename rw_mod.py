import os.path
import log
import user_interface as ui


db_file = 'database.csv'
db_book = []
last_id = 0


def read_file():
    global db_book, db_file, last_id
    if os.path.exists(db_file):
        f = open(db_file, 'r', encoding='utf-8')
        data = f.read().splitlines()
        for line in data:
            line = line.split(';')
            db_book.append(line)
        f.close()
        last_id = int(db_book[-1][0])
        return db_book
    else:
        log.logging.error('Incorrect file')
        ui.show_error_file()


def write_file(new_data):
    f = open(db_file, 'w', encoding='utf-8', newline='\n')
    for i in range(len(new_data)):
        input_line = ''
        for j in range(len(new_data[i])):
            input_line = ';'.join(new_data[i][j])
            input_line.strip()
        f.writelines(input_line)
    f.close()


def add_data(new_data):
    f = open(db_file, 'a', encoding='utf-8', newline='\n')
    input_line = ';'.join((new_data[i]) for i in range(len(new_data)))
    input_line.strip()
    f.writelines(input_line)
    f.close()

