# generators
# a list is an iterable / a generator is an iterable / but a generator is not a list
# not every iterable is a list / a generator is a subset of an iterable


def make_list(num):  # This is a list
    result = []
    for i in range(num):
        result.append(i*2)
    return result


my_list = make_list(100)
# print(my_list)


def generator_function(n):
    for i in range(n):
        yield i*2

# for item in generator_function(10):
#     print(item)

g = generator_function(10)
next(g)
next(g)
print(next(g))
print(next(g))
next(g)
print(next(g))
print(next(g))
next(g)
next(g)
print(next(g))
# next(g) # Exeption StopIteration