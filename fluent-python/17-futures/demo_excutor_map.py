# -*- coding: utf-8 -*-


from time import sleep, strftime
from concurrent import futures

from crayons import red, green, blue, yellow


def display(*args):
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)


def loiter(n):
    msg = red('{}loiter({}): doing nothing for {}s...')
    display(msg.format('\t'*n, n, n))
    sleep(n)
    msg = green('{}loiter({}): done.')
    display(msg.format('\t'*n, n))
    return n * 10


def main():
    display('Script starting.')
    executor = futures.ThreadPoolExecutor(max_workers=3)
    results = executor.map(loiter, range(1, 6))
    display(yellow('results:'), yellow(results))
    display(blue('Waitting for individual results:'))
    for i, result in enumerate(results):
        display('result {}: {}'.format(i, result))


if __name__ == '__main__':
    main()
