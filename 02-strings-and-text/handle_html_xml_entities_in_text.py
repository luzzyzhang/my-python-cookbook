import html
s = 'Elements are written as "<tag>Text</tag>".'
print(s)
print(html.escape(s))
# Disable escaping of quotes
print(html.escape(s, quote=False))
print(50*'*')
t = 'Spicy Jalapeño'
nt = t.encode('ascii', errors='xmlcharrefreplace')
print(nt)
print(50*'~')
s = 'Spicy &lt;&quot;Jalape&#241;o&quote.&gt'
from html.parser import HTMLParser
p = HTMLParser()
print(p.unescape(s))
t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))
