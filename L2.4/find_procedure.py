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

if __name__ == '__main__':
    migrations = 'Migrations'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    search_dir = os.path.join(current_dir, migrations)
    os.chdir(search_dir)
    ext = '.sql'
    files = [i for i in os.listdir(search_dir) if ext in i]
    list_my = []
    while True:
        counter = 0
        s = input('Filter:')
        if not s: break
        for fname in files:
            with open(fname, encoding='utf-8') as f:
                if s in f.read():
                    print(fname)
                    list_my.append(fname)
                    counter += 1
                    f.close()
                    files = list_my
        print('Файлов всего', counter)