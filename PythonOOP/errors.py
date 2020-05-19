# Error Handling


# while True:
#     try:
#         age = int(input('What is your age? '))
#         10/age
#     except ValueError:
#         print('Please enter a number:')
#     except ZeroDivisionError:
#         print('Please enter age higher than 0:')
#     else:
#         print('Thank you!')
#         break

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'Please enter numbers! + {err}')


print(sum('1', 2))
