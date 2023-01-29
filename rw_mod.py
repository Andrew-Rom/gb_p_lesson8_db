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
        log.logging.info('Datafile was read successfully')
        return db_book
    else:
        log.logging.error('Incorrect file')
        ui.show_error_file()


def write_file(new_db):
    f = open(db_file, mode='w', encoding='utf-8')
    input_lines = []
    for item in new_db:
        input_line = ';'.join((item[i]) for i in range(len(item)))
        input_lines.append(input_line)
    f.writelines("%s\n" % line for line in input_lines)
    f.close()
    log.logging.info('New datafile was created')


def add_data(new_data):
    f = open(db_file, 'a', encoding='utf-8', newline='\n')
    input_line = ';'.join((new_data[i]) for i in range(len(new_data)))
    f.write('\n' + input_line)
    f.close()
    log.logging.info('New data was written')

