from functools import reduce


# map, filter, zip and reduce

my_list = [1, 2, 3]
your_list = [10, 20, 30]
their_list = (5, 4, 3)


def multiply_by2(item):
    return item*2


def check_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    return acc + item


# map
print("Result for the map function is:\n", list(map(multiply_by2, my_list)), "\n")


# filter
print("Result for the filter function is:\n", list(filter(check_odd, my_list)), "\n")


# zip
print("Result for the zip function is:\n", list(zip(my_list, your_list)), "\n")
print("Result for the zip function is:\n", list(zip(my_list, your_list, their_list)), "\n")

# reduce
print("Result for the reduce function is:\n", reduce(accumulator, my_list, 0), "\n")


