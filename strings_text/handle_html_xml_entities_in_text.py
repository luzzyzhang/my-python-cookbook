import html
s = 'Elements are written as "<tag>Text</tag>".'
print(s)
print(html.escape(s))
# Disable escaping of quotes
print(html.escape(s, quote=False))
