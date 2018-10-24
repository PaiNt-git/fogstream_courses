# -*- coding: utf-8 -*-
"""


"""
# words - хранит в себе строку с словами
l = len(words)
first = words[:((l // 2) + (0 if l % 2 == 0 else 1))]
second = words[-(l // 2):]
result = second + first
print(result)
