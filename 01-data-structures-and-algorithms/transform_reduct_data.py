# Excute a reduction funciton (e.g. sum(), min(), max()),
# But first need to transform and filter the data
nums = [1, 2, 3, 4, 5]
result = sum(x * x for x in nums)
print result


# Determine if any .py files exist on a direcotry
import os
files = os.listdir('.')
# files = os.listdir('..')
if any(name.endswith('.py') for name in files):
    print "Yes we find Python code"
else:
    print "Sorry my commander"


# Output a tuple as CSV
s = ('ACME', 500, 123.45)
print ','.join(str(x) for x in s)


# Data reduction across fields of a data structure
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'ADL', 'shares': 20},
    {'name': 'AAL', 'shares': 50},
    {'name': 'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print min_shares
min_shares_name = min(portfolio, key=lambda s: s['shares'])
print min_shares_name
min_test = min(portfolio)
print min_test
