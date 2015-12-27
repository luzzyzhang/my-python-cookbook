# search and replace a pattern in string
# simple patterns use str.replace() method
text = 'zhanglu say zhaolingpu ni hai hao ma?'
n_text = text.replace('say', '@')
print n_text
# for more complicated pattern use sub() funtion/mothod in re module
# replace 11/20/2011 tot 2011-11-20
import re
date = 'Today Merry Christams 12/25/2015, I remenber you 11/25/2007'
new_date = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', date)
print new_date
# perform repeat substitutions
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
date2 = datepat.sub(r'\3-\1-\2', date)
print date2

# More complicated substitutions to specify a substitution callback function
from calendar import month_abbr


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
date3 = datepat.sub(change_date, date)
print date3

# Use re.subn() to show how many substitutions were replaced
newdate, n = datepat.subn(r'\3-\1-\2', date)
print newdate
print n
