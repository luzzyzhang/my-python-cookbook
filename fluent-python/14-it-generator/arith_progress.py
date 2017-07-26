# -*- coding: utf-8 -*-


class ArithmeticProgression(object):
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end   # None -> "infinite" series

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


def test_arithmethic_progress(begin, step, end=None):
    ap = ArithmeticProgression(begin, step, end)
    print(list(ap))


if __name__ == '__main__':
    test_arithmethic_progress(0, 1, 3)
    test_arithmethic_progress(1, .5, 3)
    test_arithmethic_progress(0, 1/3, 1)
    from fractions import Fraction
    test_arithmethic_progress(0, Fraction(1, 3), 1)
    from decimal import Decimal
    test_arithmethic_progress(0,  Decimal('.1'), .3)
