# -*- coding: utf-8 -*-
"""


"""
# array хранит список, func - функцию, init - начальное значение
# init может как передаваться в функцию reduce, так и не передаваться
# не удаляйте функцию reduce, напишите свою реализацию


def reduce_recursive(array, func, init):
    if not init:
        array = [init] + array
    x = None
    y = None
    if len(array):
        x = array.pop(0)
    if len(array):
        y = array.pop(0)
    array = ([func(x, y)] + array) if not y is None else [x]
    if len(array) == 1:
        return array[0]
    else:
        reduce_recursive(array, func, None)


def reduce_iter(array, func, init):
    iterator = iter(array)
    if init is None:
        if len(array):
            init = next(iterator)
    ccum = init
    for item in iterator:
        ccum = func(accum_value, item)
    return ccum


def reduce(array, func, init):
    return reduce_iter(array, func, init)
