# Error Handling

while True:
    try:
        age = int(input('What is your age? '))
        10/age
    except ValueError:
        print('Please enter a number:')
    except ZeroDivisionError:
        print('Please enter age higher than 0:')
        break
    else:
        print('Thank you!')
    finally:
        print('******************************')
