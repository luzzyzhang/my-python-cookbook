# Make all of the strings have the same underlying representation
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
if s1 == s2:
    print(s1 == s2)
else:
    print("False")
print(len(s1))
print(len(s2))
print(50*'*')
import unicodedata
# NFC characters should be fully composed(use a single code point)
# NFD characters should be fully decomposed(use of combine chatacters)
# NFC(normalize fully composed), NFD(normalize fully decomposed)
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print(ascii(t1))
print(ascii(t2))
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4)
print(ascii(t3))
print(ascii(t4))
print(50*'-')
# Normalizatin forms NFKC and NFKD
s = '\ufb01'
print(s)
print(unicodedata.normalize('NFD', s))
# combined letters are broken apart
print(unicodedata.normalize('NFKD', s))
print(unicodedata.normalize('NFKC', s))
print(50*'=')
# Sanitizing and filtering text, example remove all diacritical marks from text
t1 = unicodedata.normalize('NFD', s1)
nt = ''.join(c for c in t1 if not unicodedata.combining(c))
print(nt)
