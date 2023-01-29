import os.path
import log
import user_interface as ui
import csv

db_file = 'database.csv'
db_book = []
last_id = 0


def read_file():
    global db_book, db_file, last_id
    if os.path.exists(db_file):
        with open(db_file, mode='r', encoding='utf-8', newline='') as file:
            reader = csv.reader(file)
            db_book = [line for line in reader]
        last_id = int(db_book[-1][0])
        return db_book
    else:
        log.logging.error('Incorrect file')
        ui.show_error_file()


def write_file(new_db):
    with open(db_file, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for line in new_db:
            writer.writerow(line)
    log.logging.info('New datafile was created')


def add_data(new_data):
    with open(db_file, mode='a', encoding='utf-8', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(new_data)
    log.logging.info('New data was written')
