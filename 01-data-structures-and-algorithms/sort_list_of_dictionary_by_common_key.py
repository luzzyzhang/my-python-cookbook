# A list of dictionaries to sort the entries
# according to one or more of the dictionary values
from operator import itemgetter
rows = [
    {'fname': 'Brain', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
# use itemgetter() a bit faster run
# rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_uid = sorted(rows, key=itemgetter('uid'))
min_row_uid = min(rows, key=itemgetter('uid'))
# rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
print rows_by_fname
print 50*'~'
print rows_by_uid
print 50*'~'
print rows_by_lfname
print 50*'~'
print min_row_uid
