from timeit import timeit
t1 = timeit('math.sqrt(2)', 'import math')
t2 = timeit('sqrt(2)', 'from math import sqrt')
print(t1, t2)
