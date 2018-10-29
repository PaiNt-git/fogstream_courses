# -*- coding: utf-8 -*-
"""


"""
# array хранит список, func - функцию
# не удаляйте функцию map, напишите свою реализацию


def map(array, func):
    return [func(x) for x in array]
