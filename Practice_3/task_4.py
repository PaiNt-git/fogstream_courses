# -*- coding: utf-8 -*-
"""


"""
# x хранит число
# не удаляйте функцию avaranger, напишите свою реализацию


def avaranger(x):
    if not hasattr(avaranger, "pool"):
        avaranger.pool = []
    avaranger.pool.append(x)
    return sum(avaranger.pool) / len(avaranger.pool)
