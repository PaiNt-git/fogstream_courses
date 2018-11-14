# -*- coding: utf-8 -*-
"""


"""
# filename - хранит в себе имя файла

import math

lengths = []


with open(filename, "rt", encoding="utf-8") as f:
    f.seek(0)
    for line in f:
        x1, y1, x2, y2, *_ = map(float, line.split(' '))
        lengths.append(math.sqrt(
            (x2 - x1) ** 2 \
            + (y2 - y1) ** 2
        ))

min = min(lengths)
max = max(lengths)