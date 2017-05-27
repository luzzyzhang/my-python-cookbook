# Create string which embeded variable names are substituted
# with a string representation of a variable's value
s = '{name} has {n} messages'
print(s.format(name="zlp", n=1314))
name = "luzzyzhang"
n = 19911111
print(s.format_map(vars()))  # Olny work python3


class Info():
    def __init__(self, name, n):
        self.name = name
        self.n = n
a = Info('luzzy', '18')
print(s.format_map(vars(a)))
# format() and format_map() do not work with missing values
# print(s.format(name="Gououo"))  # KeyError
# Avoid this to define an alternative dict


class SafeSub(dict):
    def __missing__(self, key):
        return '{' + key + '}'
del n  # Make sure n is undefined
print(s.format_map(SafeSub(vars())))
# If frequently use, "frame hack"
import sys
def sub(text):
    return text.format_map(SafeSub(sys._getframe().f_locals))
name = 'IIIII'
n = 10086
print(sub('Hello {name}'))
print(sub('Ok {n} aa'))
print(sub('You favor aha {color}'))
# Not best
girl = 'LZP'
m = 1314
# print('%(girl) has %(m) messages.' % vars())
import string
s = string.Template('$girl has $m messages.')
ns = s.substitute(vars())
print(ns)
