from fnmatch import fnmatch, fnmatchcase
print fnmatch('foo.txt', '*.txt')
print fnmatch('foo.txt', '?oo.txt')
print fnmatch('Dat45.csv', 'Dat[0-9]*')
names = ['Dat1.csv', 'Dat2.csv', 'config.int', 'foo.py']
new_names = [name for name in names if fnmatch(name, 'Dat*.csv')]
print new_names

# If case-sensitivity
# On OS X (mac)
print fnmatch('foo.txt', '*.TXT')
# On windwos
# fnmatch('foo.txt', '*.TXT')  # True
# Use fnmatchcase() both lower and uppercase
print fnmatchcase('foo.txt', '*.TXT')

# Processing data nonfilename strings
addresses = [
    '5486 N CLark ST',
    '10087 W SAT ST',
    '10098 M SOOP AT',
    '10024 E AFFFF VT',
    '10038 A VVVC SA'
]

new_addr = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print new_addr
pattern = '54[0-9][0-9] *CLark*'
addrs2 = [addr for addr in addresses if fnmatchcase(addr, pattern)]
print addrs2
