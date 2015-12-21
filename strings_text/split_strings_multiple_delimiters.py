# split() method of string object work on simple cases,not allow for multiple
# delimiters or account of possible whitespaces around delimiters
import re
line = 'asdf fjdk; afed, fjek,asdf,         foo'
new_line = re.split(r'[:,\s]\s*', line)
print new_line
fields = re.split(r'(;|,|\s)\s*', line)
print fields
values = fields[::2]
delimiters = fields[1::2] + ['']
print values
print delimiters
# Reform the line using the same delimiters
s = ''.join(v+d for v, d in zip(values, delimiters))
print s
match = re.split(r'(?:,|;|\s)\s*', line)
print match
