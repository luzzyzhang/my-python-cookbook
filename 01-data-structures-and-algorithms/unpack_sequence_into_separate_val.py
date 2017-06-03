# Any sequence(or iterable) can be unpacked into variables
# Number of variables adn structure match the sequence
p = (4, 5)
x, y = p
print x, y
data = ['ZA', 55, 88.0, (2015, 12, 11)]
name, shares, price, date = data
print name, shares, price, date
name, shares, price, (year, mon, day) = data
print year, mon, day
# Upanck work any object iterable, tuples string files iterators generators
s = 'hello'
a, b, c, d, e = s
print a, b, c, d, e
# Discard certain values just pick a throwaway variable name
data = ['ZA', 55, 88.0, (2015, 12, 11)]
_, shares, price, _ = data
print shares, price
