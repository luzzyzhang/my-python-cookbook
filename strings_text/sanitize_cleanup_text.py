s = 'p\xfdt\u0125\xf6\xf1\x0cis\tawesome\r\n'
print(s)
# Clean up whitespace
remap = {ord('\t'): ' ', ord('\f'): ' ', ord('\r'): None}
a = s.translate(remap)
print(a)
# Strip diacritical marks
import unicodedata
import sys
# Create a dictionary to map every Unicode combing character to None
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))
# print(cmb_chrs)
b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chrs))
# Translate table maps all Unicode decimal digit characters to equal ASCII
digitmap = {c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode)
            if unicodedata.category(chr(c)) == 'Nd'}
print(len(digitmap))
# Arabic digits
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))
