# -*- coding: utf-8 -*-
"""


"""
# words - хранит в себе строку с словами
eii = len(words) - 1
result = "".join([x for i, x in enumerate(words) if ((i + 1) % 3 != 0 or i == eii)])
