# Access list or tuple elements by postions, but this make difficult do read
# a times. Less dependent on position by accessing the elements by name
from collections import namedtuple


Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('luzzyzhang@galaxy.com', '2015-11-30')
print sub
print sub.addr
print sub.joined
print len(sub)
addr, joined = sub
print addr
print joined


# Using ordinary tuples
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


# Using namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_total(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total
s = Stock('AAAA', 10010, 11.11)
print s
# s.shares = 75  # nameetuple is immutable
s = s._replace(shares=75)
print s


# _replace() method can be populate named tuples that have optional or
# missing fields
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)
# Function to convert a dictionary to a Stock


def dict_to_stock(s):
    return stock_prototype._replace(**s)
dct_a = {'name': 'PPOT', 'shares': 100, 'price': 123.45}
print dict_to_stock(dct_a)
dct_b = {'name': 'MMM', 'shares': 22, 'price': 222.2, 'date': '12/17/2015'}
print dict_to_stock(dct_b)
