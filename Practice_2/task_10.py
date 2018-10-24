# -*- coding: utf-8 -*-
"""


"""
# numbers - хранит в себе список чисел

elem, index = numbers[0], 0

for i, e in enumerate(numbers):
    if e > elem:
        elem = e
        index = i

result = elem + index