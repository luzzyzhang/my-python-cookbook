# -*- coding: utf-8 -*-
import math
from array import array


class Vector2d(object):
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    print(v1.x, v1.y)
    # x, y = v1
    # (3.0, 4.0)
    assert v1 == Vector2d(3.0, 4.0)
    v1_clone = eval(repr(v1))
    assert v1 == v1_clone
    print(v1)
    octest = bytes(v1)
    # >>> octest
    assert abs(v1) == 5.0
    assert bool(v1) is True
    assert bool(Vector2d(0, 0)) is False
