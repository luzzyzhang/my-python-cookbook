# If match simple literals can use basic string methods
text = 'yeah, but no, but yeah, but no, but yeah'
# Exact match
print text == 'yeah'
# Match at start or end
print text.startswith('yeah')
print text.endswith('no')
# Search for the location of the first occurence
print text.find('no')
# For complicated matching user regular expressions and re module
import re
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
# Simple match: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print 'yes we can'
else:
    print 'Oh no'

if re.match(r'\d+/\d+/\d+', text2):
    print 'yes we can'
else:
    print 'Oh no'
# Perform a lot of matches using the same pattern, precompile the
# regular expression pattern into a pattern object first
datepat = re.compile(r'\d+/\d+/\d+')
print datepat
if datepat.match(text1):
    print 'yes we sure can'
else:
    print 'Of course not'
if datepat.match(text2):
    print 'yes we can?'
else:
    print 'Oo may be no'
# match() method always try to find the match at the start of a string,
# If search text for all occurrences of a pattern, user findall() method
text = 'Today is 24/12/2015. Pythonic Happy Hacking KeyBord on 23/23/2016.'
match = datepat.findall(text)
print 50*'*'
print match
# Group by enclose parts of the pattern in parentheses
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print 50*'~'
print m
# Extract the contents of each groups
print m.group(0)
print m.group(3)
print m.groups()
month, day, year = m.groups()
print month, day, year
print 50*'-'
all_match = datepat.findall(text)
print all_match
for month, day, year in all_match:
    print '{}-{}-{}'.format(month, day, year)
# findall() method find all matches, return them as list,
# If match iteractively user finditer() method 
print 50*'='
print datepat.finditer(text)
for m in datepat.finditer(text):
    print m.groups()
