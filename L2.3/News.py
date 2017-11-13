#!/usr/bin/env python
# coding: utf-8
def read_files(name):
    import chardet
    with open(name, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        original_text = data.decode(result['encoding'])
        return original_text


def count_words(original_text):
    to_list = original_text.split(' ')
    words_value = {}
    for words in to_list:
        if len(words) > 6:
            if words in words_value:
                words_value[words] += 1
            else:
                words_value[words] = 1
                return words_value

def sort_top(word_value):
    l = lambda word_value: word_value[1]
    sort_list = sorted(word_value.items(), key = l, reverse = True)
    count = 1
    top_10 = {}
    for word in sort_list:
        top_10[count] = word
        count += 1
        if count == 10:
            break
    return top_10

def count_word(param):
    pass

def main():
    while True:
        name = input('Введите имя файла: newsfr.json, newsit.json, newsafr.json, newscy.json. Выход - exit: ')
        if name == 'newsfr.json' or name == 'newsit.json' or name == 'newsafr.json' or name == 'newscy.json':
            print('Идет обработка файла ...')
            top_10 = sort_top(count_word(read_files(name)))
            for i in top_10.values():
                print(i[1], ': ', i[0])
        elif name == 'exit':
            break
        else:
            print('Некорректный ввод, повторите.')


main ()
