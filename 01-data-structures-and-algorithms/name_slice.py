# rcords = ''
# SHARES = slice(20, 30)
# PRICE = slice(40, 48)
# 
# cost = int(records[SHARES]) * float(records[PRICE])
items = [ i for i in range(7)]
a= slice(2, 4)
print items[a]
print items[2:4]
items[a] = [10, 11]
print items
print 50*'*'
b = slice(10, 50, 2)
print b.start
print b.stop
print b.step
print 50*'~'

s = 'HelloWorld'
print b.indices(len(s))
for i in range(*b.indices(len(s))):
    print s[i]
