# search and replace a pattern in string
# simple patterns use str.replace() method
text = 'zhanglu say zhaolingpu ni hai hao ma?'
n_text = text.replace('say', '@')
print n_text
# for more complicated pattern use sub() funtion/mothod in re module
# replace 20/11/2011 tot 2011-11-20
import re
date = 'Today Merry Christams 25/12/2015, I remenber you 09/08/2007'
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', date)
