# -*- coding: utf-8 -*-


# http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python
class UpperAttrMetaclass(type):
    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases,
                                                      uppercase_attr)


class Foo(object):
    __metaclass__ = UpperAttrMetaclass
