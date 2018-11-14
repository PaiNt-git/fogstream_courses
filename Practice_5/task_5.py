# -*- coding: utf-8 -*-
"""


"""
# filename - хранит в себе имя исходного файла
# outfilename - хранит в себе имя файла результата

LATIN = 'zxcvbnmasdfghjklqwertyuiop'


with open(filename, "r", encoding="utf-8") as f:
    content = f.read()
    chars = ''.join(filter(lambda x: x.lower() in LATIN, set(content)))


with open(outfilename, "a", encoding="utf-8") as f:
    for char in chars:
        cnt = content.count(char)
        f.write(f'{char} {cnt}\n')