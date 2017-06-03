# Check the start or end of a string for specific text patterns,
# such as filename extensions, URL schemes, and so on
# Use startswith(), endswith() methods
filename = 'sapm.txt'
filename.endswith('.txt')
filename.startswith('file:')
url = 'http://www.python.org'
url.startswith('http:')
# If check multiple choices use tuple
import os
filenames = os.listdir('.')
print filenames
specific = [name for name in filenames if name.endswith(('.txt', '.py'))]
print specific
py = any(name.endswith('.py') for name in filenames)
print py

# from urllib.request import urlopen  # python3
from urllib2 import urlopen


def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()
read_data("http://www.baidu.com")
# startswith first arg must be str or tuple of str
choices = ['http:', 'ftp:']
url = 'http://www.luzzyzhang.coom'
# TypeError
# url.startswith(choices) 
url.startswith(tuple(choices))
# Check direcotry for the presence of certain kinds of files
# if any(name.endswith(('.c', '.py')) for name in listdir(dirname)):


# Not elegant way
filename = 'spam.txt'
filename[-4:] = '.txt'
url = 'http:www.baidu.com'
url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:'
# Work but not better
import re
url = 'http://www.python.org'
re.match('http:|https:|ftp:', url)
