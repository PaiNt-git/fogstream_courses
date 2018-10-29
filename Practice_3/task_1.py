# -*- coding: utf-8 -*-
"""


"""
# x1, x2, y1, y2 хранят координаты
# не удаляйте функцию area, напишите свою реализацию


def area(x1, x2, y1, y2):
    basis = abs(x2 - x1)
    height = abs(y2 - y1)
    result = 0.5 * basis * height
    return result
