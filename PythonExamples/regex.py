import re


pattern = re.compile(r"([A-z]).([a])")
pattern1 = re.compile('search')
string = 'search this inside of this text please!'
string1 = 'this'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string1)
d = pattern1.match(string)

print(a.group())
print(b)
print(c)
print(d)
