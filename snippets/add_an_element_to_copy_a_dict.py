# -*- coding: utf-8 -*-
"""
Google Search
how to use list comprehension to add an element to copies of a dictionary
"""


class Building(object):
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return '<{0.x}>'.format(self)

    def lst_of_dct(self, lst, common):
        # return = [dict(id=i, **self.common) for i in self.lst]

        # This way raise SyntaxError: non-keyword arg after keyword arg
        # return [dict(mid=i, common) for i in self.lst]
        return [dict(common, mid=i) for i in lst]


def foo(lst):
    return map(Building, lst)


if __name__ == '__main__':
    """
    :input: ids = [1, 2, 3, 4], SomeClass(), common = {'we': 'one'}
    :output: [{'id': 1, 'we': 'one'}, {'id': 2, 'we': 'one'}, ...]
    """
    lst1 = [1, 2, 3, 4]
    print(foo(lst1))
    b = Building(2)
    print(b.lst_of_dct(lst1, {'we': 'one'}))
