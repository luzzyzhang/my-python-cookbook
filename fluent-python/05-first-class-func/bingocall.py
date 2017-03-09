"""
>>> bingo = BingoCage(range(3))
>>> bingo.pick()
0
>>> bingo()
1
>>> callable(bingo)
True
"""


import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


if __name__ == '__main__':
    bingo = BingoCage(range(10))
    print(bingo())
