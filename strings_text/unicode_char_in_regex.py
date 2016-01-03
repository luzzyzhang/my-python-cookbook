# use regex process text handle unicode character
import re
num = re.compile('\d+')
# ASCII digits
print num.match('123')
# Arabic digits
print num.match('\0661\0662\0663')
# Include specific characters in pattern,escape sequence for unicode data
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')
# Normalize all text to a standard
pat = re.compile('stra\u00dfe', re.IGNORECASE)
print \u00df
# print pat.match(s)
# print s.upper()
# print pat.match(s.upper())
