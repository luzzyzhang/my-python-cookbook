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
