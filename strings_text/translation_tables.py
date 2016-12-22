# -*- coding: utf-8 -*-
import string


table = string.maketrans('ABC', '123')
f = 'A + B == C'
print f.translate(table)
print eval(f.translate(table))
