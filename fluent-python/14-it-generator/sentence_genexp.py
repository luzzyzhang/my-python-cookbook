# -*- coding: utf-8 -*-


import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence(object):
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence({})'.format(reprlib.repr(self.text))

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))
