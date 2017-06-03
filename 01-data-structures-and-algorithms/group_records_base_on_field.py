from operator import itemgetter
from itertools import groupby
from collections import defaultdict
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2015'},
    {'address': '5148 N CLARK', 'date': '07/04/2015'},
    {'address': '5800 E 58TH', 'date': '07/02/2015'},
    {'address': '2122 N CLARK', 'date': '07/03/2015'},
    {'address': '5645 N HELLO', 'date': '07/02/2015'},
    {'address': '1060 W ADDIO', 'date': '07/02/2015'},
    {'address': '4810 N BBICO', 'date': '07/01/2015'},
    {'address': '1039 W GRANT', 'date': '07/04/2015'},
]


# Sort by the desired field first
rows.sort(key=itemgetter('date'))
print rows

# Iterate in groups, groupby return a iterator the same values in a group
for date, items in groupby(rows, key=itemgetter('date')):
    print date
    print items
    print 50*'~'
    for i in items:
        print '****', i

# Use defaultdcit
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
print rows_by_date
for r in rows_by_date['07/02/2015']:
    print r
