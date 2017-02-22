# -*- coding: utf-8 -*-


class Pair(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


if __name__ == '__main__':
    pair = Pair(1, 2)
    pair
    print(pair)
    # special !r formatting code indicates that the output of __repr__
    # should be used instead of __str__()
    print('p is {0!r}'.format(pair))
    print('p is {0}'.format(pair))
