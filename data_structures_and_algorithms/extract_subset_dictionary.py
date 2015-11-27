# Extracting a Subset of a Dictionary
prices = {'ACME': 45.25, 'AAPL': 612.78, 'GOOG': 10,
          'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}

# Make new dictionary of all prices over 200
new_prices1 = {key: value for key, value in prices.items() if value > 200}
print new_prices1
# Make a new dictionary of tech company name
tech_names = ['AAPL', 'IBM', 'HPQ', 'MSFT']
new_prices = {key: value for key, value in prices.items() if key in tech_names}
print new_prices
