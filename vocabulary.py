# coding: utf-8

import os


en_ru = {}
if os.path.exists("mydict.py"):
    import mydict
    en_ru = mydict.en_ru


def fill_dict(en_ru):
    while new_word != "": 
		new_word = input("Введите слово ")
		new_translate = input("Введите перевод ")

		if new_word not in en_ru and new_word != "":
			en_ru[new_word] = new_translate
    return

print(en_ru)
