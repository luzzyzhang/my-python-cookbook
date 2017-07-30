# -*- coding: utf-8 -*-

"""
In a generator decorated with @contextmanager, yield is used to split the body
of the function in two parts: everything before the yield will be executed at
the beginning of the while block when the interpreter calls __enter__;
the code after yield will run when __exit__ is called at the end of the block.
"""


import contextlib


@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    sys.stdout.write = original_write


def test():
    with looking_glass() as what:
        print('ABC, DEF')
        print(what)
    print(what)


if __name__ == '__main__':
    test()
