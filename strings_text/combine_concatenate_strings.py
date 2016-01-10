# Combine many small strings together into a larger string
# If strings in a sequence or iterable, fastest way to combine
# strings use join() method
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
parts2 = ("Happy", "Hack", "Day", "And", "Night")
print '-'.join(parts2)
print ' '.join(parts)
print ','.join(parts)
print ''.join(parts)
# If only combine a few strings use + work well
a = "Is Python"
b = "And Golang"
c = "Of course C++"
print a + '  ' + b + ',' + c
s = '{}~{}'.format(a, b)
s1 = a + '~' + b
print s
print s1
t = 'Hello' 'World'
print t
print 50*'*'
data = ['ACME', 10, 199.1]
# print ','.join(data)  # error
data_str = ','.join(str(d) for d in data)  # convert int or float to sting
print data_str
# print(a + ':' + b + ':' + c)  # ugly
# print(':'.join([a, b, c]))  # still ugly
# print(a, b, c, seq=':')  # better
# Mixing I/O operations and string concatenation
# Version 1 (string concatenation)
# If two strings are small better performance tan version 2
'''
f.write(chunk1 + chunk2)
'''
# Version 2 (separate I/O operations)
# If two strings are large better performance than version 1
'''
f.write(chunk1)
f.write(chunk2)
'''
print 50*'-'


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicageo'
text = ','.join(sample())
print text
with open('test.txt', 'w') as f:
    for part in sample():
        print part
        f.write(part)


print 50*'*'
# Combination of parts into buffers and larger I/O operations


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield '$'.join(parts)
            parts = []
            size = 0
    yield '-'.join(parts)

with open('test2.txt', 'w') as f:
    for part in combine(sample(), 32768):
        print 50*'='
        print part
        print 50*'='
        f.write(part)
