# -*- coding: utf-8 -*-

s = 'ABC'  # iterable
for char in s:
    print(char)

# Emulate the for machinery by hand

it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break
