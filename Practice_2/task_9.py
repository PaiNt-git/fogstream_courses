# -*- coding: utf-8 -*-
"""


"""
# numbers - хранит в себе список чисел


def test_znak(a, b):
    if a > 0 and b > 0:
        return True
    elif a < 0 and b < 0:
        return True
    return False

result = [(numbers[i - 1], x) for i, x in enumerate(numbers) if i != 0 and test_znak(x, numbers[i - 1])]
result = sum(result[0]) if len(result) >= 1 else 0
