# # Задание
# 7  # мне нужно отыскать файл среди десятков других
# 8  # я знаю некоторые части этого файла (на память или из другого источника)
# 9  # я ищу только среди .sql файлов
# 10  # 1. программа ожидает строку, которую будет искать (input())
# 11  # после того, как строка введена, программа ищет её во всех файлах
# 12  # выводит список найденных файлов построчно
# 13  # выводит количество найденных файлов
# 14  # 2. снова ожидает ввод
# 15  # поиск происходит только среди найденных на этапе 1
# 16  # 3. снова ожидает ввод
# 17  # ...
# 18  # Выход из программы программировать не нужно.
# 19  # Достаточно принудительно остановить, для этого можете нажать Ctrl + C
# 20
#
# 21  # Пример на настоящих данных
# 22
#
# 23  # python3 find_procedure.py
# 24  # Введите строку: INSERT
# 25  # ... большой список файлов ...
# 26  # Всего: 301
# 27  # Введите строку: APPLICATION_SETUP
# 28  # ... большой список файлов ...
# 29  # Всего: 26
# 30  # Введите строку: A400M
# 31  # ... большой список файлов ...
# 32  # Всего: 17
# 33  # Введите строку: 0.0
# 34  # Migrations/000_PSE_Application_setup.sql
# 35  # Migrations/100_1-32_PSE_Application_setup.sql
# 36  # Всего: 2
# 37  # Введите строку: 2.0
# 38  # Migrations/000_PSE_Application_setup.sql
# 39  # Всего: 1
# 40
#
# 41  # не забываем организовывать собственный код в функции


import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))


def sql_file(file_name):
    return os.path.splitext(file_name)[1] == '.sql'


def file_open(path_file):
    with open(path_file) as f:
        file_str = f.read()
        return file_str


def sql_files(search):
    sql_list = []
    for root, dirs, files in os.walk(search):
        for file in files:
            if sql_file(file):
                sql_list.append(os.path.join(root, file))
    return sql_list


def check_string(searching_string, string_file):
    return searching_string in string_file


def list_of_result(searching_string, path_list):
    result_of_search = []
    for file_path in path_list:
        file_string = file_open(file_path)
        if check_string(searching_string, file_string):
            result_of_search.append(file_path)
    return result_of_search


if __name__ == '__main__':

    search_dir = os.path.join(current_dir, migrations)
    new_search_list = sql_files(search_dir)
    while True:
        searching_string = input('Введите строку:\n')
        new_search_list = list_of_result(searching_string, new_search_list)
        print('\n'.join(new_search_list))
        print('Всего: ', len(new_search_list))
