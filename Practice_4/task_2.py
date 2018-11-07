# -*- coding: utf-8 -*-
"""


"""
# напишите реализацию класса Polynome


class Polynome:
    _koeffs = []

    def __init__(self, koeffs):
        self._koeffs = koeffs[:]

    def __add__(self, other):
        sk = self._koeffs[:]
        ok = other._koeffs[:]
        sl = len(sk)
        ol = len(ok)

        if sl > ol:
            ok = ok + [0] * (sl - ol)
        elif ol > sl:
            sk = sk + [0] * (ol - sl)

        sl = ol = len(sk)

        sk = [sk[i] + ok[i] for i in range(sl)]
        new_poly = Polynome(sk)
        return new_poly

    def __sub__(self, other):
        sk = self._koeffs[:]
        ok = other._koeffs[:]
        sl = len(sk)
        ol = len(ok)

        if sl > ol:
            ok = ok + [0] * (sl - ol)
        elif ol > sl:
            sk = sk + [0] * (ol - sl)

        sl = ol = len(sk)

        sk = [sk[i] - ok[i] for i in range(sl)]
        new_poly = Polynome(sk)
        return new_poly

    def __mul__(self, other):
        sk = self._koeffs[:]
        ok = other._koeffs[:]
        sl = len(sk)
        ol = len(ok)

        if sl > ol:
            ok = ok + [0] * (sl - ol)
        elif ol > sl:
            sk = sk + [0] * (ol - sl)

        sl = ol = len(sk)

        res_koeffs = []
        res_powers = []
        for i in range(sl):
            for j in range(ol):
                res_koeffs.append(sk[i] * ok[j])
                res_powers.append(i + j)

        max_pow = max(res_powers)
        min_pow = min(filter(lambda x: x >= 0, res_powers))

        reduce_koeffs = [0] * (max_pow + 1 - min_pow)
        for i in range(min_pow, max_pow + 1):
            for j in range(len(res_powers)):
                if not res_powers.count(i):
                    break
                index = res_powers.index(i)
                if index >= 0:
                    koeff = res_koeffs.pop(index)
                    pow_ = res_powers.pop(index)
                    reduce_koeffs[pow_] = reduce_koeffs[pow_] + koeff
                else:
                    break

        new_poly = Polynome(reduce_koeffs)
        return new_poly

    def calc(self, x):
        return sum([(koeff * (x ** pow_)) for pow_, koeff in enumerate(self._koeffs)])