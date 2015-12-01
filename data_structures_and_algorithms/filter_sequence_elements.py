# Use list comprehension
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
positive_list = [n for n in mylist if n > 0]
print positive_list
negative_list = [n for n in mylist if n < 0]
print negative_list
# Use generator expressions
pos = (n for n in mylist if n > 0)
print pos
for p in pos:
    print p

values = ['1', '2', '3', '4', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print ivals


# Transform the data
import math
sqr_lst = [math.sqrt(n) for n in mylist if n > 0]
print sqr_lst

clip_neg = [n if n > 0 else 0 for n in mylist]
print clip_neg
clip_pos = [n if n < 0 else 0 for n in mylist]
print clip_pos

# Filter one sequence to another related sequence
# make list all addresses corresponding count value was greater than 5
addresses = [
    '5412 N CLARK',
    '5418 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress
more5 = [n > 5 for n in counts]
print more5
new_address = list(compress(addresses, more5))
print new_address
