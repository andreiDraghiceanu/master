import random

# return random number
print(random.random())

# return random integer between a min and max
print(random.randint(0, 10))

# choose from a list
print(random.choice([1, 2, 3, 4, 5]))

# random
my_list = [1, 2, 3, 4, 5]
print(random.shuffle(my_list))
print(my_list)
