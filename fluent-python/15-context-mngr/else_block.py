# -*- coding: utf-8 -*-
"""This is just demo code
"""

# for ... else ...
for item in my_list:
    if item.flavor == 'bananas':
        break
else:
    raise ValueError('No banana flavor found')


try:
    dangerous_call()
    after_call()
except OSError:
    log('OSError ...')

# VS

# For clarity and correctness, the body of a try block should only have the
# statements that may generate the expected exceptions. This is much better:
try:
    dangerous_call()
except OSError:
    log('OSError ...')
else:
    after_call()
