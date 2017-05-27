# -*- coding: utf-8 -*-


class decorator_without_args(object):

    def __init__(self, f):
        print('Inside __init__()')
        self.f = f

    def __call__(self, *args):
        """The __call__ method is not called until the decorator function is called.
        """
        print('Inside __call__()')
        self.f(*args)
        print('After serlf.f(*args)')


class decorator_with_args(object):
    def __init__(self, arg1, arg2, arg3):
        """If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print('Inside __init__()')
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        """If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        print('Inside __call__()')

        def wrappedf(*args):
            print('Inside wrappedf()')
            print('Decorator args:', self.arg1, self.arg2, self.arg3)
            f(*args)
            print('After f(*args)')
        return wrappedf


@decorator_without_args
def say_hello(a1, a2, a3, a4):
    print('Hello args:', a1, a2, a3, a4)


@decorator_with_args('知识', '啊哈', 42)
def hello(a1, a2, a3, a4):
    print('Hello args:', a1, a2, a3, a4)


if __name__ == '__main__':
    print("After decoration")
    print(20*'.' + ' 不带参数 ' + 20*'.')
    print(50*'-')
    print("Preparing to call say_hello()")
    say_hello("say", "hello", "argument", "list")
    print("After first say_hello() call")
    print(50*'*')
    say_hello("a", "different", "set of", "arguments")
    print("After second say_hello() call")
    print(20*'-' + ' 带参数 ' + 20*'-')
    print("After decoration")
    print(50*'-')
    print("Preparing to call hello()")
    hello("say", "hello", "argument", "list")
    print("After first hello() call")
    print(50*'*')
    hello("a", "different", "set of", "arguments")
    print("After second say_hello() call")
