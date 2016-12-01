# -*- coding: utf-8 -*-

# 1.How do we use generators?
# 2.What is a generator expressions/function/object?
# 3.When and why do we use generator?

# Example problem: compute the summ of the
# squares of the integers from 1 to 1 million


# Use function, too messy it clutters up the program, especially use once
def sumsqures(n):
    squres = []
    for x in range(n):
        squres.append(x**2)
    return sum(squres)


# Generator function not a normal function
def gensqures(n):
    i = 0
    while i <= n:
        yield i**2
        i += 1


if __name__ == '__main__':
    # Normal functon too messy
    print sumsqures(1000001)
    print 50*'-'

    # List comprehension use too much memory
    print sum([x**2 for x in range(1000001)])
    print 50*'-'

    # Use gengerator expression
    print sum((x**2 for x in range(1000001)))
    g = (x**2 for x in range(11))
    print g, next(g), next(g), next(g)
    print sum(g)
    g = (x**2 for x in range(11))
    for i in g:
        print i
    print 50*'-'

    # Use generator function
    print gensqures(11)
    print next(gensqures(11)), next(gensqures(11)), next(gensqures(11))
    gs = gensqures(11)
    print next(gs), next(gs), next(gs)
