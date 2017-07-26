# -*- coding: utf-8 -*-

import itertools


def aritprog_gen(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    return ap_gen


def test_aritprog_gen(begin, step, end=None):
    print(list(aritprog_gen(begin, step, end)))


if __name__ == '__main__':
    test_aritprog_gen(1, 0.5, 3)
