# -*- coding: utf-8 -*-

from functools import reduce

# set & | - ^
a = {1, 2, 3}
b = {2, 4, 5}
print(a & b, a | b, a - b, a ^ b)
l1 = [1, 2, 3]
l2 = [2, 4, 5, 3]
l3 = [2, 3, 0, 1]
s1, s2 = set(l1), set(l2)
print(s1 & s2, s1 | s2, s1 - s2, s1 ^ s2)

lst = [set(l1), set(l2), set(l3)]
print(set.intersection(set(l1), set(l3)))
print(set.intersection(*lst))
print(reduce(lambda x, y: set(x) & set(y), lst))
