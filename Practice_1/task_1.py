# -*- coding: utf-8 -*-
"""
1.Дано число n. С начала суток прошло n минут. Определите, сколько часов и
минут будут показывать электронные часы в этот момент. Программа должна
вывести два числа: количество часов (от 0 до 23) и количество минут (от 0
до 59). Учтите, что число n может быть больше, чем количество минут в сутках.
"""


def main(n):
    hours, memainder = n // 60, n % 60

    days, homainder = hours // 24, hours % 24

    return (homainder, memainder) if days >= 1 else ((hours, memainder))


if __name__ == '__main__':

    ninput = None
    while ninput is None:
        ninput = input('Ведите количество минут (целое):\n')
        try:
            ninput = int(ninput)
        except ValueError as err:
            if 'invalid literal for int() with base 10' in str(err):
                ninput = None
                continue

    print(main(ninput))
