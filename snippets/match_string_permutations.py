"""
    Filter a Set for Matching String Permutations
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Input: string, words(a set)
    Output: list of string
    https://stackoverflow.com/questions/44857962/filter-a-set-for-matching-string-permutations
    Base on Raymond Hettinger's solution.
"""


from collections import Counter
from itertools import permutations
from string import letters
from random import choice
from operator import mul
from time import time


def match_sort(string, words):
    target = sorted(string)
    return sorted(word for word in words if sorted(word) == target)


def match_multiset(string, words):
    target = Counter(string)
    return sorted(word for word in words if Counter(word) == target)


primes = [2, 3, 5, 7, 11]
primes += [p for p in range(13, 1620) if all(pow(b, p-1, p) == 1 for b in (5, 11))]
anagram_hash = lambda s: reduce(mul, (primes[ord(c)] for c in s))


def match_perfect_hash(string, words):
    target = anagram_hash(string)
    return sorted(word for word in words if anagram_hash(word) == target)


def match_permutations(string, words):
    perms = set(map(''.join, permutations(string)))
    return sorted(word for word in words if word in perms)


def match_permutations_set(string, words):
    perms = set(map(''.join, permutations(string)))
    return sorted(words & perms)


string_size = 5
words_size = 1000000


population = letters[: string_size+2]
words = set()

for i in range(words_size):
    word = ''.join([choice(population) for i in range(string_size)])
    words.add(word)
string = word                # Arbitrarily search use the last word as the target

print('Timings with string_size=%d and words_size=%d' % (string_size, words_size))
for func in (match_sort, match_multiset, match_perfect_hash, match_permutations, match_permutations_set):
    start = time()
    func(string, words)
    end = time()
    print('%-10.5f %s' % (end - start, func.__name__))