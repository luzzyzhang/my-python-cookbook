# -*- coding: utf-8 -*-

"""
https://stackoverflow.com/questions/773/how-do-i-use-pythons-itertools-groupby
https://docs.python.org/3/library/itertools.html#itertools.groupby
"""


from itertools import groupby


things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"),
          ("vehicle", "speed boat"), ("vehicle", "school bus")]


for key, group in groupby(things, lambda x: x[0]):
    for thing in group:
        print("A %s is a %s." % (thing[1], key))
    print("-"*50)


for key, group in groupby(things, lambda x: x[0]):
    lst_of_things = " and ".join(thing[1] for thing in group)
    print(key + "s: " + lst_of_things + ".")


# Equivalent to
class my_groupby:
    # [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
    # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
    def __init__(self, iterable, key=None):
        if key is None:
            key = lambda x: x
        self.keyfunc = key
        self.it = iter(iterable)
        self.tgtkey = self.currkey = self.currvalue = object()

    def __iter__(self):
        return self

    def __next__(self):
        while self.currkey == self.tgtkey:
            self.currvalue = next(self.it)    # Exit on StopIteration
            self.currkey = self.keyfunc(self.currvalue)
        self.tgtkey = self.currkey
        return (self.currkey, self._grouper(self.tgtkey))

    def _grouper(self, tgtkey):
        while self.currkey == tgtkey:
            yield self.currvalue
            try:
                self.currvalue = next(self.it)
            except StopIteration:
                return
            self.currkey = self.keyfunc(self.currvalue)

print([k for k, g in my_groupby('AAAABBBCCDAABBB')])   # --> A B C D A B
print([list(g) for k, g in my_groupby('aaaabbbccd')])  # --> aaaa bbb cc d
