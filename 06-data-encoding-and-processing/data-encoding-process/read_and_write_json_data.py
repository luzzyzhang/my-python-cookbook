# -*- coding: utf-8 -*-


import json
import decimal


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super().default(o)


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def encode_complex(obj):
    if isinstance(obj, complex):
        return [obj.real, obj.imag]
    raise TypeError(repr(obj) + " is not JSON serializable")


if __name__ == '__main__':
    p = Point(2, 3)
    # json.dumps(p)
    print(json.dumps(2 + 1j, default=encode_complex))
    print(json.JSONEncoder(default=encode_complex).encode(2 + 1j))
    print(json.dumps({'x': decimal.Decimal('5.5')}, cls=DecimalEncoder))
