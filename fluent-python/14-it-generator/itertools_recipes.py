# -*- coding: utf-8 -*-

"""https://docs.python.org/3/library/itertools.html#itertools-recipes
"""

import collections
from itertools import (islice, count, repeat, combinations, filterfalse,
                       cycle, groupby, chain, starmap, tee, zip_longest)


def take(n, iterable):
    return list(islice(iterable, n))


def tabulate(function, start=0):
    return map(function, count(start))


def tail(n, iterable):
    "Return an iterator over the last n items"
    return iter(collections.deque(iterable, maxlen=n))


def consume(iterator, n):
    "Advance the iterator n-steps ahead. If n is none, consume entirely."
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)


def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)


def all_equal(iterable):
    "Returns True if all the elements are equal to each other"
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def padnone(iterable):
    return chain(iterable, repeat(None))


def flatten(list_of_lists):
    return chain.from_iterable(list_of_lists)


def repeat_func(func, times=None, *args):
    if times is None:
        return starmap(func, repeat(args))
    return starmap(func, repeat(args, times))


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    pending = len(iterables)
    nexts = cycle(iter(it).__next__ for it in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = cycle(islice(nexts, pending))


def partition(pred, iterable):
    'Use a predicate to partition entries into false entries and true entries'
    # partition(is_odd, range(10)) --> 0 2 4 6 8   and  1 3 5 7 9
    t1, t2 = tee(iterable)
    return filterfalse(pred, t1), filter(pred, t2)


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


if __name__ == '__main__':
    # print(take(3, 'ABCDEF'))
    # print(list(tail(3, iter('ABCDEFG'))))
    # print(nth(range(10), 3, default=10086))
    # print(all_equal('ABCDEF'),
    #       all_equal(['AAAA', 'AAAA']),
    #       all_equal({'a', 'a'}),
    #       all_equal({'a': 1, 'b': 1}.values()))
    # print(list(flatten([['a', 'b', 'c'], [1, 2, 3]])))
    # print(list(repeat_func(lambda x, y: (y, x), 3, 'Hello', 'World')))
    # print(list(pairwise([0, 1, 2, 3, 4, 5, 6])))
    # print([''.join(g) for g in grouper('ABCDEFG', 3, 'x')])
    # print(list(roundrobin('ABC', 'D', 'EF')))
    # for part in partition(lambda x: x % 2, range(10)):
    #     print(list(part))
    print(list(powerset([1, 2, 3])))
