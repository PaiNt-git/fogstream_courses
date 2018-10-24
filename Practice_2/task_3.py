# -*- coding: utf-8 -*-
"""


"""
# words - хранит в себе строку с словами
fc = words.count("f")
ff = words.find("f")
result = ff if fc <= 1 else (ff + words.rfind("f"))
