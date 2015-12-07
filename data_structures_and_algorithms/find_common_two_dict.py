a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}
# Find common keys in common
c = a.keys() & b.keys()
# Find keys in a that are not in b
d = a.keys() - b.keys()
# Find (key, value) pairs in common
e = a.items() & b.items()
print c
print d
# Make a new dictionary with certain keys removed
f = {key: a[key] for key in a.keys() - {'z', 'w'}}
