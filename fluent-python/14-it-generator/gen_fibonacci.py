# -*- coding: utf-8 -*-


def fibonacci():
    # A generator to produce the Fibonacci series
    # which because it is infinite, would never fit in a collection.
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


def fibonacci2(n):
    # Fibnacci series up to n
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    from itertools import islice
    print(list(islice(fibonacci(), 4)))
    print(list(fibonacci2(10)))
