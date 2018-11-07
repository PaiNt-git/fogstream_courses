# -*- coding: utf-8 -*-
"""


"""
# напишите реализацию класса Point3D

import math


class Point3D:
    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, other):
        if not isinstance(other, Point3D):
            raise ValueError

        return math.sqrt(
            (self.x - other.x) ** 2 \
            + (self.y - other.y) ** 2 \
            + (self.z - other.z) ** 2
        )