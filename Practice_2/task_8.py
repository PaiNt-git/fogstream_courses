# -*- coding: utf-8 -*-
"""


"""
# numbers - хранит в себе список чисел
result = [x for i, x in enumerate(numbers) if (i != 0 and x > numbers[i - 1])]
