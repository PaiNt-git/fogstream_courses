# -*- coding: utf-8 -*-
"""


"""
# numbers - хранит в себе список чисел
# number - хранит в себе случайное число

sorted_students = sorted(students, key=lambda x: x['grade'])

grades_rating = sorted(list(set([x['grade'] for x in students])))

result = [x['name'] for x in sorted_students if x['grade'] == grades_rating[1]]