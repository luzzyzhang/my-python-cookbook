# -*- coding: utf-8 -*-

"""
https://docs.python.org/3/library/itertools.html#itertools.islice
"""

import sys
from itertools import islice


def test_generator():
    for i in range(10):
        yield i


# Equivalent to
def my_islice(iterable, *args):
    s = slice(*args)
    it = iter(range(s.start or 0, s.stop or sys.maxsize, s.step or 1))
    try:
        nexti = next(it)
    except StopIteration:
        return
    for i, element in enumerate(iterable):
        if i == nexti:
            yield element
            nexti = next(it)


if __name__ == '__main__':
    # print(test_generator()[:2])
    print(islice(test_generator(), 0, 2))
    assert list(islice(test_generator(), 0, 2)) == [0, 1]
    print(50*'~')
    print(my_islice(test_generator(), 0, 3))
    assert list(my_islice(test_generator(), 1, 3)) == [1, 2]
