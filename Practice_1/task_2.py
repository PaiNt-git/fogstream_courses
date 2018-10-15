# -*- coding: utf-8 -*-
"""
2.Длина Московской кольцевой автомобильной дороги —109 километров. Стартуем
с нулевого километра МКАД и едем со скоростью V километров в час. На какой
отметке остановимся через T часов? Программа получает на вход значение V и
T. Если V>0, то движемся в положительном направлении по МКАД, если же
значение V<0, то в отрицательном. Программа должна вывести целое число от 0
до 108 — номер отметки, на которой остановимся.
"""

MOSCOW_LENGTH = 109.0


def main(v, t):
    sign = -1 if (abs(v) != v) else 1

    l = v * t

    lemainder = l % MOSCOW_LENGTH

    return sign * int(lemainder)


if __name__ == '__main__':

    vinput = None
    while vinput is None:
        vinput = input('Введите скорость, км/ч (целое или с точкой):\n')
        try:
            vinput = float(vinput)
        except ValueError as err:
            if 'could not convert string to float' in str(err):
                vinput = None
                continue

    tinput = None
    while tinput is None:
        tinput = input('Введите время, ч (целое или с точкой, не отрицательное):\n')
        try:
            tinput = float(tinput)
        except ValueError as err:
            if 'could not convert string to float' in str(err) or tinput < 0:
                tinput = None
                continue

    print(main(vinput, tinput))
