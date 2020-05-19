# this is a comment
print('Hello world')
print('Hello\' again\\ Newline: \n Tab: \t')

s = """Hello \"""hello"
world
Hello
again"""

print(s)

raw_string = r'\n \t \ '
print(raw_string)

n = 0
if n < 10:
    print('lower than 10')
    print('same if branch')
elif n < 30:
    print('lower than 30')
else:
    print('all other cases')


i = 0
while i < 10:
    print(i)
    i += 2
    if i == 6:
        break
else:
    print('else')

print('Last value', i)


s = 'Bună ziua. Ce zi frumoasă'
count_a = 0
for char in s:
    if char == 'a':
        continue
    print(char)


for pos in range(len(s)):
    print(pos)
    if pos == 10:
        break


for nr in range(3, 9, 2):
    print(nr)
