# -*- coding: utf-8 -*-
"""
3.В некоторой школе занятия начинаются в 9:00. Продолжительность урока — 45
минут, после 1-го, 3-го, 5-го и т.д. уроков перемена 5 минут, а после 2-го,
4-го, 6-го и т.д. — 15 минут. Дан номер урока (число от 1 до 10).
Определите, когда заканчивается указанный урок. Выведите два целых числа:
время окончания урока в часах и минутах.
"""

LESSONS_BEGIN_HOUR = 9
LESSONS_BEGIN_MINUTE = 0
MAX_LESSONS_DAY = 10


def main(n):
    five_range = list(range(1, MAX_LESSONS_DAY + 1, 2))
    fivteen_range = list(range(2, MAX_LESSONS_DAY + 1, 2))

    minutes = 0
    for nless in range(1, n + 1):
        minutes += 45
        if nless < n:
            if nless in five_range:
                minutes += 5
            elif nless in fivteen_range:
                minutes += 15

    absbegin_minute = LESSONS_BEGIN_HOUR * 60 + LESSONS_BEGIN_MINUTE
    full_minute = absbegin_minute + minutes

    hours, memainder = full_minute // 60, full_minute % 60

    return (hours, memainder)


if __name__ == '__main__':

    ninput = None
    while ninput is None:
        ninput = input('Ведите номер урока (целое 1..10):\n')
        try:
            ninput = int(ninput)
            if ninput < 1 or ninput > 10:
                ninput = None
                continue
        except ValueError as err:
            if 'invalid literal for int() with base 10' in str(err):
                ninput = None
                continue

    print(main(ninput))
