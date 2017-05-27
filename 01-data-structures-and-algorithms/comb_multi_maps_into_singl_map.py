'''Multiple dictionaries or mapping to logically combine into a single mapping
to perform certain operations, sunch as looking up values or checking exist key
'''


from collections import ChainMap
# Only work for python3, ChainMap since python3.3


a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)
print(len(c))
print(list(c.keys()))
print(list(c.values()))
print(c)
print(c['x'])
print(c['y'])
print(c['z'])


values = ChainMap()
values['x'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])
# Discard last mapping
values = values.parents
print(values['x'])
# Discard last mapping
values = values.parents
print(values['x'])
print(values)


# Merging dictionaries together using update() method
merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged['y'])
print(merged['z'])
# original dic mutate the changes don't get reflected in merged dict.
# a['x'] = 13
# print(merged['x']

# ChainMap user original dict
chain_merged = ChainMap(a, b)
print(chain_merged['x'])
a['x'] = 10086
print(chain_merged['x'])
