# comprehensions

# my_list = []
#
# for char in 'hello':
#     my_list.append(char)
#
# print(my_list)

my_list = [char for char in 'hello']
my_list2 = [num for num in range(0, 100)]
my_list3 = [num*2 for num in range(0, 100)]
my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]

print(my_list4)


my_set = {char for char in 'hello'}
my_set2 = {num for num in range(0, 100)}
my_set3 = {num*2 for num in range(0, 100)}
my_set4 = {num**2 for num in range(0, 100) if num % 2 == 0}

print(my_set)

simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {key: value**2 for key, value in simple_dict.items()}
my_dict1 = {key: value**2 for key, value in simple_dict.items() if value % 2 == 0}
my_dict3 = {num: num*2 for num in [1, 2, 3]}

print(my_dict)
print(my_dict1)
print(my_dict3)

