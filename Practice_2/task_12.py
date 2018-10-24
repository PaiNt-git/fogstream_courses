# -*- coding: utf-8 -*-
"""


"""
# numbers - хранит в себе список чисел
# number - хранит в себе случайное число
numbers.append(number)
numbers.sort()
numbers.reverse()
# интересно почему не работает чтот типа numbers.index(number, -1, 0) :) ?
result = len(numbers) - numbers.index(number) - 1