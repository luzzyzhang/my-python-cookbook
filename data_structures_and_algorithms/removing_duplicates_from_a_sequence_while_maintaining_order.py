# This only work if the items in the sequence are harshble.
lst = [2, 1, 3, 1, 1, 2, 5, 9, 9, 10, 5]


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
nlst = list(dedupe(lst))
print nlst


# If sequence of unhashable types (such as dicts)
l_dct = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3},
         {'x': 1, 'y': 2}, {'x': 2, 'y': '4'}]


def dedupe_unhash(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
nl_dct = list(dedupe_unhash(l_dct, key=lambda d: (d['x'], d['y'])))
print nl_dct
nl_dct2 = list(dedupe_unhash(l_dct, key=lambda d: d['x']))
print nl_dct2
