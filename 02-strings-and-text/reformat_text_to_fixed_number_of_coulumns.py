# Long strings to reformat specified number of columns
s = "Look into my eyes, look into my eye, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
import textwrap
print textwrap.fill(s, 50)
print 50*'*'
print textwrap.fill(s, 40, initial_indent='    ')
print 50*'~'
print textwrap.fill(s, 40, subsequent_indent='    ')
# Only python3
import os
print os.get_terminal_size().columns
