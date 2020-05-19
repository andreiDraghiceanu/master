# Ex 1
l = ['a', 'b', 'c']
my_string = ''.join(l)
print(my_string)


# Ex 2
def count_distinct(l):
    count = 1 if l else 0

    for i in range(len(l)-1):
        if l[i] != l[i+1]:
            count += 1

    return count

    # for elem in l:
    #     if l.count(elem) > 1:
    #         l.remove(elem)

    # return len(l)


assert count_distinct([1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 5]) == 5
assert count_distinct([]) == 0


# Ex 3
def common_element(list1, list2):
    out = False
    for elem in list1:
        if elem in list2:
            out = True
            break
    return out


assert common_element([1, 2, 3], [2, 4, 5]) is True
assert common_element([1, 2, 3], [8, 4, 5]) is False


# Ex 4
def filter_long_words(words_list, min_length):
    long_words = []
    for word in words_list:
        if len(word) > min_length:
            long_words.append(word)
    return long_words


lista_cuvinte = ['hello', 'ana', 'banana', 'a']
l = filter_long_words(lista_cuvinte, 3)
print(l)
print(lista_cuvinte)
print(l is lista_cuvinte)
