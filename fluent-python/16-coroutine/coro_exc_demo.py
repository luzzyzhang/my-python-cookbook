# -*- coding: utf-8 -*-

from inspect import getgeneratorstate


class DemoException(Exception):
    """An exception type for the demonstration."""


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine recieved: {!r}'.format(x))
    raise RuntimeError('This line should never run.')


# some clean up code
def demo_finally():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled Countinuing...')
            else:
                print('-> coroutine received: {!r}'.format(x))
    finally:
        print('-> coroutine ending')


def test_coro_close():
    exc_coro = demo_exc_handling()
    next(exc_coro)
    exc_coro.send(11)
    exc_coro.send(22)
    exc_coro.close()
    print(getgeneratorstate(exc_coro))


def test_coro_thow():
    exc_coro = demo_exc_handling()
    next(exc_coro)
    exc_coro.send(11)
    exc_coro.throw(DemoException)
    print(getgeneratorstate(exc_coro))

    try:
        exc_coro.throw(ZeroDivisionError)
    except ZeroDivisionError:
        print(getgeneratorstate(exc_coro))


if __name__ == '__main__':
    test_coro_close()
    print(50*'-')
    test_coro_thow()
