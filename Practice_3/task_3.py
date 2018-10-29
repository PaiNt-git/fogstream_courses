# -*- coding: utf-8 -*-
"""


"""
# scores хранит список результатов
# не удаляйте функцию stronger, напишите свою реализацию


def stronger(scores):
    count = 0
    for i in range(1, len(scores)):
        if scores[i - 1] < scores[i]:
            count += 1
    return count
