def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

lsts = [1, 2, 3, 3, 2, 5, 3, 4, 4]
nlst = list(dedupe(lsts))
print nlst


dcts = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3},
        {'x': 1, 'y': 2}, {'x': 2, 'y': '4'}]


def dedupe_unhash(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

ndcts = list(dedupe_unhash(dcts, key=lambda d: (d['x'], d['y'])))
print ndcts
ndcts2 = list(dedupe_unhash(dcts, key=lambda dct: dct['y']))
print ndcts2
ndcts3 = list(dedupe_unhash(dcts, key=lambda d: d['x']))
print ndcts3
