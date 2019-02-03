# coding: utf-8

import os


en_ru = {}
if os.path.exists("mydict.py"):
    import mydict
    en_ru = mydict.en_ru


def fill_dict(en_ru):
    # side-effect: en_ru is being changed here
    return

print(en_ru)
