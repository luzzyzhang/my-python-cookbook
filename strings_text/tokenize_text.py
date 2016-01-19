# Parse string left to right into a stream of tokens
# text = 'foo = 23 + 42 * 10'
# Turn the string into a sequence of pairs like this:
tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'),
          ('PLUS', '+'), ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
print '|'.join([NAME, NUM, PLUS, TIMES, EQ, WS])
scanner = master_pat.scanner('foo = 42')
print scanner.match()
from collections import namedtuple
Token = namedtuple('Token', ['type', 'value'])


def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())
# Example use
for tok in generate_tokens(master_pat, 'foo = 42'):
    print tok
print 50*'~'
text = 'foo = 23 + 42 * 10'
tokens = (tok for tok in generate_tokens(master_pat, text) if tok.type != 'WS')
for tok in tokens:
    print tok
