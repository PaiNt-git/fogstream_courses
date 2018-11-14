# -*- coding: utf-8 -*-
"""


"""
# filename - хранит в себе имя файла

import re

letters = 0
words = 0
rows = 0

letter_pattern = re.compile(r'[a-zA-Z]')
word_pattern = re.compile(r'\b[a-zA-Z]+\b')


with open(filename, "rt", encoding="utf-8") as f:
    f.seek(0)
    for line in f:
        match_letter = letter_pattern.findall(line)
        if match_letter:
            letters += len(match_letter)

        match_word = word_pattern.findall(line)
        if match_word:
            words += len(match_word)

        rows += 1