# -*- coding: utf-8 -*-
"""


"""
# напишите реализацию класса Complex


class Complex:
    real = 0
    imag = 0

    def __init__(self, real, imag):
        # if not isinstance(real, int) or not isinstance(imag, int):
        #     raise ValueError('real or imag are not int')

        self.real = real
        self.imag = imag

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return Complex(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return Complex(real, imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        first_numerator = self.real * other.real + self.imag * other.imag
        second_numerator = self.imag * other.real - self.real * other.imag

        denominator = other.real ** 2 + other.imag ** 2

        real = first_numerator / denominator
        imag = second_numerator / denominator
        return Complex(real, imag)

    def __str__(self):
        znak = '+' if self.imag >= 0 else ''
        real = self.real
        imag = self.imag
        return f'({real:0>.2f}{znak}{imag:0>.2f}j)'