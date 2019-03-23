import math

# choice = input("Choose from: ")
# choices = list()
# for i in choice:
#     choices.append(i)
#     while " " in choices:
#         choices.remove(" ")
#
# choices[i] = int(choices[i])
# print(choices)


a = 123

a = (a//(10**i))%10
for i in range(math.ceil(math.log(a, 10))-1, -1, -1):
    print(a)