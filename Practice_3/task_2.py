# -*- coding: utf-8 -*-
"""


"""
# x хранит число
# не удаляйте функцию is_pow, напишите свою реализацию


def count(start=0):
    while True:
        yield start
        start += 1


def is_int_pow(x, base):
    while x > 1 and x % base == 0:
        x = x / base
        if x <= 1:
            return True
    return False


def is_pow(x):
    # x = y ** z, где x ~ [2; 1000]
    end_y = 1000
    for y in count(2):
        if is_int_pow(x, y) and y != x:
            return True
        if y > end_y:
            break

    return False
