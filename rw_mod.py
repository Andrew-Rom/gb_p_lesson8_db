# чтение
def read_file(file):
    f = open('database.cvs', 'r', encoding='utf-8')
    data = f.read().splitlines()
    list = []
    for line in data:
        line = line.split(';')
        list.append(line)
    f.close()
    return list

# Запись
def rewrite_file(list):
    f = open('database.cvs', 'w', encoding='utf-8')
    for i in range(len(list)):
        for j in range(len(list[i])):
            f.writelines(list[i][j])
            f.writelines(';')
        f.writelines('\n')
    f.close()
    return list

# Дозапись
def write_file(list):
    f = open('database.cvs', 'a', encoding='utf-8')
    for i in range(len(list)):
        for j in range(len(list[i])):
            f.writelines(list[i][j])
            f.writelines(';')
        f.writelines('\n')
    f.close()
    return list

