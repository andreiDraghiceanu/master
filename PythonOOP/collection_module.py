from collections import Counter, defaultdict, OrderedDict


li = [1, 1, 2, 3, 3, 3, 4, 7, 7, 7,  5, 6, 7]
li1 = ['a', 'a', 'b', 'c', 'c', 'd', 'c']
print(Counter(li))
print(Counter(li1))


dictionary = defaultdict(lambda: 5, {'a': 1, 'b': 2})
print(dictionary['c'])


d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d == d2)
