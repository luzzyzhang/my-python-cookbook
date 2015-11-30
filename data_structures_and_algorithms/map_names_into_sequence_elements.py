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
