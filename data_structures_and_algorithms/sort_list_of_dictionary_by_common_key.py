# A list of dictionaries to sort the entries
# according to one or more of the dictionary values
from operator import itemgetter
rows = [
    {'fname': 'Brain', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print rows_by_fname
print 50*'~'
print rows_by_uid
print 50*'~'
print rows_by_lfname
