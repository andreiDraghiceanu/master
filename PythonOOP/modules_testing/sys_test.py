import sys
import random

first_number = int(sys.argv[1])
second_number = int(sys.argv[2])


random_number = random.randint(first_number, second_number)


while True:
    number = int(input("Please enter the number: ", ))
    if number == random_number:
        break
