# -*- coding: utf-8 -*-

lst = []
lst1 = [1, 2, 3]
lst2 = [1, '', 3]
lst3 = ['', None, False, ' ', 0]   # if ' ' --> True
print(all(lst), all(lst1), all(lst2), all(lst3))
print(any(lst), any(lst1), any(lst2), any(lst3))


# all() equivalent to
def my_all(iterable):
    for element in iterable:
        if not element:
            return False
    return True


# any() equivalent to
def my_any(iterable):
    for element in iterable:
        if element:
            return True
    return False


print(my_all(lst), my_all(lst1), my_all(lst2), my_all(lst3))
print(my_any(lst), my_any(lst1), my_any(lst2), my_any(lst3))
