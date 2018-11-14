# -*- coding: utf-8 -*-
"""


"""
# filename - хранит в себе имя файла

import re

lect = 0
pract = 0
lab = 0

day_pattern = re.compile(r'^\b(?P<weekday>[\w\s.]+)\b(?!\s*\()$')
subject_pattern = re.compile(r'^\b(?P<subjet>[\w .]+)\b\s*(?=\((?P<subject_type>[\w.]+)\))')


with open(filename, "rt", encoding="utf-8") as f:
    f.seek(0)
    for line in f:
        match_day = day_pattern.search(line)
        if not match_day:
            match_subject = subject_pattern.search(line)
            if match_subject:
                subject_type = match_subject.group('subject_type')
                if subject_type == 'лекц.':
                    lect += 1
                elif subject_type == 'практ.':
                    pract += 1
                elif subject_type == 'лаб.':
                    lab += 1