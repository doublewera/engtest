# coding: utf-8

import os


en_ru = {}
if os.path.exists("mydict.py"):
    import mydict
    en_ru = mydict.en_ru


def fill_dict(en_ru):
    new_word = None
    # side-effect: en_ru is being changed here
    while new_word != "":
        new_word = input("Введите слово ")
        new_translate = input("Введите перевод ")

        if new_word not in en_ru and new_word != "":
            en_ru[new_word] = new_translate
    return



def save_dict(en_ru, dict_file_name="mydict.py"):
    mydict = open(dict_file_name, "w")
    mydict.write("en_ru = %s" % en_ru)
    mydict.close()
    return

fill_dict(en_ru)
save_dict(en_ru)
print(en_ru)
