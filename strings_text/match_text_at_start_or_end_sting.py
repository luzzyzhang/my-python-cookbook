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

