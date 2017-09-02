# -*- coding: utf-8 -*-

"""
Curio spinner
~~~~~~
https://github.com/dabeaz/curio
"""

import sys
import itertools

import curio


async def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            await curio.sleep(.1)
        except curio.CancelledError:
            break
    write(' ' * len(status) + '\x08' * len(status))


async def slow_function():
    # pretend waiting a long time for I/O
    await curio.sleep(3)
    return 42


async def supervisor():
    spinner = await curio.spawn(spin('thinking!'))
    print('spinner object:\n', repr(spinner))
    result = await slow_function()
    await spinner.cancel()
    return result


def main():
    result = curio.run(supervisor)
    print('Answer:', result)


if __name__ == '__main__':
    main()
