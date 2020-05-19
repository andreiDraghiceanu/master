from functools import reduce
# lambda expressions

# lambda param: action(param)


my_list = [1, 2, 3]
your_list = [10, 20, 30]
their_list = (5, 4, 3)

list_s = [(0, 2), (4, 3), (9, 9), (10, -1)]

# def multiply_by2(item):
    # return item*2
print(list(map(lambda item: item * 2, my_list)))


# def check_odd(item):
   # return item % 2 != 0
print(list(filter(lambda item: item % 2 != 0, my_list)))


# def accumulator(acc, item):
   # return acc + item
print(reduce(lambda acc, item: acc + item, your_list))


print(list(map(lambda item: item*item, my_list)))

print(sorted(list_s, key=lambda item: item))

