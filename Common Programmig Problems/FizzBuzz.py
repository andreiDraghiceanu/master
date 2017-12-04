for num in range(0, 101):
    if (num % 3 == 0 and num % 2 == 0):
        print('FizzBuzz')
    elif num % 2 == 0:
        print('Buzz')
    elif num % 3 == 0:
        print('Fizz')
    else:
        print('This is not divisible with 2 or 3!!!')

            
