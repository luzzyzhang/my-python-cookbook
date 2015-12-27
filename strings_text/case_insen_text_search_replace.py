# Search replace text in a case-insensitive manner
import re
text = 'UPPER PYTHON, lower python, Mixed Python'
find_py = re.findall('python', text, flags=re.IGNORECASE)
print find_py
new_text = re.sub('python', 'Golang', text, flags=re.IGNORECASE)
print new_text


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

texts = 'UPPER PYTHON, lower python, Mixed Python'
case_replace = re.sub('python', matchcase('snake'), texts, flags=re.IGNORECASE)
print case_replace
