# -*- coding: utf-8 -*-
"""


"""
# напишите реализацию класса Fraction


class Fraction:
    a = 0
    b = 1

    def __init__(self, a, b):
        # if not isinstance(a, int) or not isinstance(b, int):
        #     raise ValueError('a or b are not int')
        if b == 0:
            raise ValueError('b is zero')

        self.a = a
        self.b = b

        self.cut_fract()  # maybe...

    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def cut_fract(self):
        gcd = self._gcd(self.a, self.b)
        if gcd:
            self.a = self.a // gcd
            self.b = self.b // gcd

    def common_denom(self, other):
        a = self.a * other.b
        b = other.a * self.b
        b_ = self.b * other.b
        self_ = Fraction(1, 1)
        other_ = Fraction(1, 1)
        self_.a, self_.b = a, b_
        other_.a, other_.b = b, b_
        return self_, other_

    def __add__(self, other):
        self_, other_ = self.common_denom(other)
        self_.a += other_.a
        self_.cut_fract()
        return self_

    def __sub__(self, other):
        self_, other_ = self.common_denom(other)
        self_.a -= other_.a
        self_.cut_fract()
        return self_

    def __mul__(self, other):
        a = self.a * other.a
        b = self.b * other.b
        self_ = Fraction(a, b)
        return self_

    def __eq__(self, other):
        self_, other_ = self.common_denom(other)
        return (self_.a == other_.a)

    def __gt__(self, other):
        self_, other_ = self.common_denom(other)
        return (self_.a > other_.a)

    def __le__(self, other):
        self_, other_ = self.common_denom(other)
        return (self_.a <= other_.a)
