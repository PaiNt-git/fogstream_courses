# -*- coding: utf-8 -*-
"""


"""
# напишите реализацию классов Figure, Triangle, Rectangle, Circle

import math


class Figure:

    def area(self):
        raise NotImplementedError('''
        Не определена функция площади в классе-наследнике: {}.
        '''.format(self.__class__.__name__))

    def perimeter(self):
        raise NotImplementedError('''
        Не определена функция периметра в классе-наследнике: {}.
        '''.format(self.__class__.__name__))


class Triangle(Figure):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        half_p = self.perimeter() / 2
        return math.sqrt((half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c)))

    def perimeter(self):
        return self.a + self.b + self.c


class Rectangle(Figure):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


class Circle(Figure):

    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * (self.r**2)

    def perimeter(self):
        return math.pi * 2 * self.r
