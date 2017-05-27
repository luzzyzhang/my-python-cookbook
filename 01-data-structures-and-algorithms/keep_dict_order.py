from collections import OrderedDict
dct = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4,
    'e': 5, 'f': 6, 'g': 7, 'h': 8
}
for d in dct:
    print d
print 50*'~'
# OrderDict size is more than twice as large as nomal dict
order_dct = OrderedDict()
order_dct['a'] = 1
order_dct['b'] = 2
order_dct['c'] = 3
order_dct['d'] = 4
order_dct['e'] = 5
order_dct['f'] = 6
order_dct['g'] = 7
order_dct['h'] = 8
for d in order_dct:
    print d, order_dct[d]
