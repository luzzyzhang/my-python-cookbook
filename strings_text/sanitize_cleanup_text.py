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
