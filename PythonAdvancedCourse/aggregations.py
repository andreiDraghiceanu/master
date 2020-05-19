l = [
    {'first_name': 'John', 'last_name': 'Cornwell', 'net_worth': 2632.345},
    {'first_name': 'Emily', 'last_name': 'Alton', 'net_worth': -4578.234},
    {'first_name': 'James', 'last_name': 'Bond', 'net_worth': 1000.07},
]

# min(l)  # raises TypeError - cannot compare instances of dict

# Lambda functions
# lambda *arguments: return_value
# lambda x: x * 10
# lambda x, y: x + y

# key - function applied to each element in iterable
# function results are compared, rather than iterable items
print(min(l, key=lambda x: x['net_worth']))  # element in l with minimum net_worth
print('\n')

# sort list by length of last_name
print(sorted(l, key=lambda x: len(x['last_name'])))
print('\n')

# select only elements whose first_name starts with J
for filtering in filter(lambda x: x['first_name'].startswith('J'), l):
    print(filtering)
print('\n')

# build another iterable of dicts with keys last_name and nw_tva
for mapping in map(lambda x: {'last_name': x['last_name'], 'nw_tva': x['net_worth']*1.2}, l):
    print(mapping)
print('\n')

# zip two iterables together - build iterable with elements (l[0], l[0]), (l[1], l[1]), ...
for iter in zip([1, 2, 3], [6, 7, 8, 9]):
    print(iter)
print('\n')

# get iterable with (index, value) elements from l
for enum in enumerate(l):
    print(enum)


# All objects returned by aggregation functions above are iterable, i.e. can be used in for loops:
# for x in sorted(l, key=lambda x: len(x['last_name'])):
#    print(x)
