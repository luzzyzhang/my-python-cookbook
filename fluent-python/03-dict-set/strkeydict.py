# -*- coding: utf-8 -*-
"""
>>> d = StrKeyDict([(2, 'two'), ('4', 'four')])
>>> sorted(d.keys())
['2', '4']

>>> d['2']
'two'
>>> d['4']
'four'
>>> d[1]
Traceback (most recent call last):
...
KeyError: '1'
>>> d.get('2')
'two'
>>> d.get(4)
'four'
>>> d.get(1, 'N/A')
'N/A'

>>> 2 in d
True
>>> 1 in d
False

>>> d[0] = 'zero'
>>> d['0']
'zero'

>>> d.update({6:'six', '8':'eight'})
>>> sorted(d.keys())
['0', '2', '4', '6', '8']
>>> d.update([(10, 'ten'), ('12', 'twelve')])
>>> sorted(d.keys())
['0', '10', '12', '2', '4', '6', '8']
>>> d.update([1, 3, 5])
Traceback (most recent call last):
  ...
TypeError: 'int' object is not iterable

"""
import collections


class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item


if __name__ == '__main__':
    import doctest
    doctest.testmod()
