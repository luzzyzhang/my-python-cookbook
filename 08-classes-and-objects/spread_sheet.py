# -*- coding: utf-8 -*-
# http://code.activestate.com/recipes/355045-spreadsheet/


"""
>>> from math import sin, pi
>>> SpreadSheet.tools.update(sin=sin, pi=pi, len=len)
>>> ss = SpreadSheet()
>>> ss['a1'] = '5'
>>> ss['a2'] = 'a1*6'
>>> ss['a3'] = 'a2*7'
>>> ss['a3']
210
>>> ss['b1'] = 'sin(pi/4)'
>>> ss['b1']
0.7071067811865475
>>> ss.getformula('b1')
'sin(pi/4)'
"""


class SpreadSheet:
    _cells = {}
    tools = {}

    def __setitem__(self, key, formula):
        self._cells[key] = formula

    def getformula(self, key):
        return self._cells[key]

    def __getitem__(self, key):
        return eval(self._cells[key], SpreadSheet.tools, self)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
