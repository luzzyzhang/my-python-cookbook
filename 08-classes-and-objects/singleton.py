# -*- coding: utf-8 -*-


# 0. From Peter Norvig http://norvig.com/python-iaq.html

def singleton(instance):
    klass = instance.__class__
    if hasattr(klass, '__instantiated'):
        raise ValueError("%s is a Singleton class but is already instantiated" % klass)
    klass.__instantiated = True


class MyTestClass:
    def __init__(self, *args):
        singleton(self)


# 1. Use __new__() method
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instances'):
            cls._instances = object.__new__(cls, *args, **kwargs)
        return cls._instances


# class TestClass(Singleton):
#     a = 1


# 2. Use decorator
def Singleton1(cls, *args, **kwargs):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton


# @Singleton1
# class TestClass(object):
#     a = 1


# 3. Use share attribute, just reference to the same methods and attributes
class Singleton2(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._state
        print(id(obj.__dict__))
        return obj


# class TestClass(Singleton2):
#     a = 1


# 4. Use __metaclass__
class Singleton3(type):
    def __init__(cls, name, bases, dict):
        super(Singleton3, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton3, cls).__call__(*args, **kwargs)
        return cls._instance


class TestClass(object):
    __metaclass__ = Singleton3


# 5. Python module import, this file singleton.py is a module
class MySingleton(object):
    def foo(self):
        pass


my_singleton = MySingleton()
# to use
# from singleton import my_singleton
# my_singleton.foo()


if __name__ == '__main__':
    test1 = TestClass()
    test2 = TestClass()
    # print test1.a, test2.a
    test1.a = 2
    print(test1.a, test2.a)
    print(id(test1), id(test2))
