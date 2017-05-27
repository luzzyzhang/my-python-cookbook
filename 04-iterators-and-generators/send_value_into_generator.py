# -*- coding: utf-8 -*-
def double_inputs():
    while True:
        x = yield 'aha'
        yield x * 2


gen = double_inputs()
print gen.next()
print gen.send(10)
print gen.next()
print gen.send(6)
print gen.next()
print gen.send(94.3)
