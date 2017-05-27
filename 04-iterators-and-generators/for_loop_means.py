# -*- coding: utf-8 -*-


for x in items:
    print x

# Means to
# iterable
it = iter(items)
try:
    while True:
        x = next(it)
        print x
except StopIteration:
    pass


i = 0
while i < len(items):
    x = items[i]
    print x
