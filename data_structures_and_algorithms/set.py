# -*- coding: utf-8 -*-

# set & | - ^
a = {1, 2, 3}
b = {2, 4, 5}
print a & b, a | b, a - b, a ^ b
l1 = [1, 2, 3]
l2 = [2, 4, 5]
s1, s2 = set(l1), set(l2)
print s1 & s2, s1 | s2, s1 - s2, s1 ^ s2
