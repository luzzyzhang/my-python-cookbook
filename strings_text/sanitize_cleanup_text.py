s = 'p\xfdt\u0125\xf6\xf1\x0cis\tawesome\r\n'
print(s)
remap = {ord('\t'): ' ', ord('\f'): ' ', ord('\r'): None}
a = s.translate(remap)
print(a)
# Clean up whitespace, strip diacritical marks
import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chrs))
