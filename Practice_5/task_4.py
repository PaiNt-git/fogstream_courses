# -*- coding: utf-8 -*-
"""


"""
# filename - хранит в себе имя файла
# word - искомое слово

result = 0


with open(filename, "rt", encoding="utf-8") as f:
    f.seek(0)
    for line in f:
        result += line.count(word)