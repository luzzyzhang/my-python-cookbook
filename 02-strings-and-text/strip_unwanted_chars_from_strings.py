# strip() method used to strip characters from the beginning or end of a
# string. lstrip() and rstrip() perform stripping from the left or right
# Whitespace stripping
s = '     hello world   \n'
print s.strip()
print s.lstrip()
print s.rstrip()
# Characters stripping
t = '---------hello=========='
print t.lstrip('-')
print t.rstrip('=')
print t.strip('-=')
# stripping does not apply to any text in the middle of a string
s = '    hello     world    \n'
print s.strip()
# For inner space use replace() method or regular expression substitution
print 50*'~'
s = 'hello     world    \n'
print s.replace(' ', '')
import re
print re.sub('\s+', ' ', s)
# Common use case
with open(filename) as f:
    lines = (line.strip() for line in f)
    for line in lines:
        do_something
