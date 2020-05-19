#
#
# d1 = {x: ord(x) for x in string.ascii_lowercase[:5]}
# print(d1)
#
# d2 = {v: k for k, v in d1.items()}
# print(d2)
#
# d3 = {k:v for k, v in d2.items() if k % 2 == 0}
# print(d3)
#
# d4 = {ord(x): x for x in string.ascii_lowercase[:5] if ord(x) % 2 == 0}
# print(d4)
#
# d4 = {v: k for k, v in d1.items() if v % 2 == 0}
# print(d4)


# 1. Find all of the numbers from 1-1000 that are divisible by 7.

div_7 = [div for div in range(1, 1001) if div % 7 == 0]
# print(div_7)


# 2. Find all of the numbers from 1-1000 that have a 3 in them.

num_3 = [num for num in range(1, 1000) if
         (num % 1 == 3) or (num % 100 == 3) or (num % 10 == 3) or (num // 10) % 10 == 3 or (num // 100) % 100 == 3]

# print(num_3)


# 3. Count the number of spaces in a string.

space_string = [spaces for spaces in 'Ana are   mere  bune . ' if spaces == ' ']

# print(space_string.count(' '))


# 4. Remove all of the vowels in a string.

vowels_string = [vowel for vowel in 'ana are copite.' if
                 vowel != 'a' and vowel != 'i' and vowel != 'o' and vowel != 'e' and vowel != 'u']

# print(''.join(vowels_string))


# 5. Find all of the words in a string that are less than 4 letters.

four_letters = [words for words in 'Am iesit in parc sa ma plimb cu bicicleta.'.split() if len(words) < 4]

# print(four_letters)


# 6. Use a dictionary comprehension to count the length of each word in a sentence.

words_in_sentence = {words: len(words) for words in 'Aceasta este o propozitie de test.'.split()}

# print(words_in_sentence)


# 7. Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit
# besides 1 (2-9).

div_by_digit = [number for number in range(1, 1001) if True in [True for divisor in range(2, 10) if number % divisor == 0]]

# print(div_by_digit)


# 8. For all the numbers 1-1000, use a nested list/dictionary comprehension to find the highest single digit any of
# the numbers is divisible by

highest_single_digit = {number:max([divisor for divisor in range(1,10) if number % divisor == 0]) for number in range(1,1001)}
print(highest_single_digit)