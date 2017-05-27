# Map key to more values(multidict)
# store values in container(list or set ..)
dct1 = {'a': [1, 2], 'b': [3, 4, 5]}
dct2 = {'a': {1, 2, 3}, 'b': {4, 5}}
# Use collections module defaultdict
from collections import defaultdict
dct = defaultdict(list)
dct['a'].extend([i for i in range(10)])
dct['b'] .append(5)
dct['b'].append(6)
print dct
# Or use setdefault
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(3)
print d
# defaultdict will auto create dict for keys access
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)
# Clean code
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
