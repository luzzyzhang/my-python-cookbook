# -*- coding: utf-8 -*-
"""
Note that this is not idiomatic Python, as the next refactorings will make very clear.
But it serves to make explicit the relationship between the iterable collection
and the iterator object.
"""
import re
import reprlib

RE_WORD = re.compile('\w+')


class SentenceIterable(object):
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'SentenceIterable(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator(object):
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


def test_iterable_obj(text):
    s = SentenceIterable(text)
    print(s)
    for word in s:
        print(word)

    print(list(s))
    # print(s[0], s[5], s[-1])


if __name__ == '__main__':
    text = '"The time has come," the walrus said,'
    test_iterable_obj(text)
