# split() method of string object work on simple cases,not allow for multiple
# delimiters or account of possible whitespaces around delimiters
import re
line = 'asdf fjdk; afed, fjek,asdf,         foo'
new_line = re.split(r'[:,\s]\s*', line)
print new_line
