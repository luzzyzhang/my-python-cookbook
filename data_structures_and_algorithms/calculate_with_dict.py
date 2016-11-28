# -*- coding: utf-8 -*-
# Perform calculations on dictionary data
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print min_price
print max_price
print zip(prices.values(), prices.keys())
print prices_sorted
# zip() creates an iterator can only be consumed once
prices_names = zip(prices.values(), prices.keys())
print min(prices_names)  # OK
print max(prices_names)  # Oh no
print 50*'*'
dct = {'AAA': 45.23, 'ZZZ': 45.23}
print min(zip(dct.values(), dct.keys()))
print max(zip(dct.values(), dct.keys()))
print 50*'~'
# Not well
print min(prices)
print min(prices.values())
print min(prices, key=lambda k: prices[k])
print prices[min(prices, key=lambda k: prices[k])]
