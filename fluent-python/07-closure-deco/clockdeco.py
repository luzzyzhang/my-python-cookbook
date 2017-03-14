import time


def clock(func):
    def clocked(*args):
        t0 = time.time()
        result = func(*args)
        elapsed = time.time() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s (%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


@clock
def snooze(seconds):
    time.sleep(seconds)


if __name__ == '__main__':
    print(50*'*', 'Calling snooze(.123)')
    snooze(.123)
    print(50*'*', 'Calling factorial(6)')
    print('6! =', factorial(6))
