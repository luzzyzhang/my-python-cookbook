# -*- coding: utf-8 -*-

import sys
import time
import itertools
import threading


def spin(msg, done):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        if done.wait(.1):
            break
    write(' ' * len(status) + '\x08' * len(status))


def slow_function():
    # presend waiting a long time for I/O
    time.sleep(3)
    return 42


def supervisor():
    done = threading.Event()
    spinner = threading.Thread(target=spin,
                               args=('thinking!', done))

    print('spinner object:', spinner)
    spinner.start()
    result = slow_function()
    done.set()
    spinner.join()
    return result


def main():
    result = supervisor()
    print('Answer:', result)


if __name__ == '__main__':
    main()
