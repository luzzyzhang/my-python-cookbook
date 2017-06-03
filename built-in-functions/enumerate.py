# -*- coding: utf-8 -*-


seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons, start=1)))


# Equivalent to
def my_enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

print(list(my_enumerate(seasons, start=2)))
