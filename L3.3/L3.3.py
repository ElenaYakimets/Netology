import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(text, to_lang):
    params = {'key': API_KEY, 'text': text, 'lang': to_lang, }

    response = requests.get (URL, params=params)
    json_ = response.json ()
    return ''.join (json_['text'])

def translate_my(path_in, lang='ru'):
    read_file = open (path_in, 'r')
    my_txt = read_file.read ()
    read_file.close ()
    print ('original txt:')
    print (my_txt)
    translated_txt = translate_it (my_txt, lang)
    print ('translated_txt txt:')
    print (translated_txt)
    outPath = path_in[0:2] + 'translated.txt'
    out_put = open (outPath, 'w')
    out_put.write (translated_txt)
    out_put.close ()

if __name__ == "__main__":
    translate_my ('DE.txt', 'de-ru')
    translate_my ('ES.txt', 'es-ru')
    translate_my ('FR.txt', 'fr-ru')
