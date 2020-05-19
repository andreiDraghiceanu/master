import random


def gen_random(max_nr):
    while True:
        yield random.randint(1, max_nr)


it = gen_random(5)
for i in range(10):
    print(next(it))

print('\n\n')

i = 0
for random_nr in it:
    print(random_nr)
    i += 1
    if i == 10:
        break


def gen_unique0(seq):
    unique_elems = []
    for i in seq:
        if i in unique_elems:
            continue
        unique_elems.append(i)
        yield i


def gen_unique(seq):
    for i in set(seq):
        yield i


for elem in gen_unique([1, 1, 1, 3, 5, 6, 3, 3, 5]):
    print(elem)

for elem in gen_unique("absbabasa"):
    print(elem)
