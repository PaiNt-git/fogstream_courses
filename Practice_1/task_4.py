# -*- coding: utf-8 -*-
"""
4.Процентная ставка по вкладу составляет P процентов годовых, которые
прибавляются к сумме вклада. Вклад составляет X рублей Y копеек. Определите
размер вклада через год. Программа получает на вход целые числа P, X, Y и
должна вывести два числа: величину вклада через год в рублях и копейках.
Дробная часть копеек отбрасывается.
"""

# Считаем что: начисление происходят в момент окончания вклада или на другой счет (не капитализированный процент), в задаче обратное не указано


DEPOSIT_YEARS = 1


def main(p, x, y):

    abskopek = x * 100 + y

    simp_interes = int(abskopek * DEPOSIT_YEARS * p / 100)
    abskopek += simp_interes

    rub, kop = abskopek // 100, abskopek % 100

    return rub, kop


if __name__ == '__main__':

    pinput = None
    while pinput is None:
        pinput = input('Введите процентную ставку (целое или с точкой):\n')
        try:
            pinput = float(pinput)
        except ValueError as err:
            if 'could not convert string to float' in str(err):
                pinput = None
                continue

    xinput = None
    while xinput is None:
        xinput = input('Ведите количество рублей (целое):\n')
        try:
            xinput = int(xinput)
        except ValueError as err:
            if 'invalid literal for int() with base 10' in str(err):
                xinput = None
                continue

    yinput = None
    while yinput is None:
        yinput = input('Ведите количество копеек (целое):\n')
        try:
            yinput = int(yinput)
        except ValueError as err:
            if 'invalid literal for int() with base 10' in str(err):
                yinput = None
                continue

    print(main(pinput, xinput, yinput))
