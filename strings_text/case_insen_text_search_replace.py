# Search replace text in a case-insensitive manner
import re
text = 'UPPER PYTHON, lower python, MIxed Python'
find_py  = re.findall('python', text, flags=re.IGNORECASE)
print find_py
new_text = re.sub('python', 'Golang', text, flags=re.IGNORECASE)
print new_text
