# Parse string left to right into a stream of tokens
text = 'foo = 23 + 42 * 10'
# Turn the string into a sequence of pairs like this:
tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'),
          ('PLUS', '+'), ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
