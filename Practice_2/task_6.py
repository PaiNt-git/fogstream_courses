# -*- coding: utf-8 -*-
"""


"""
# words - хранит в себе строку с словами
pangram_chars = "zxcvbnmasdfghjklpoiuytrewq"
intersect = set([x for x in words if x in pangram_chars])
result = len(pangram_chars) == len(intersect)