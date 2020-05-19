# 1. Given a list of tuples (product, price_eur), build the list of (product,
# price_ron), knowing that the exchange rate is 4.75.
####################################################################################################################

price_list = [('mere', 10), ('pere', 20), ('capsuni', 15)]
# [('mere', 10*4.75), ('pere', 20*4.75), ...]

out_list = []
for element in price_list:
    out_list.append(element[1] * 4.75)
print(out_list)


out_list = []
for element in price_list:
    tup = (element[0], element[1] * 4.75)
    out_list.append(tup)
print(out_list)


out_list = []
for product, price in price_list:
    tup = (product, price * 4.75)
    out_list.append(tup)
print(out_list)


print(list(map(lambda element: element[1] * 4.75, price_list)))
print(list(map(lambda element: (element[0], element[1] * 4.75), price_list)))


# 2. Write a function filter_short_words(word_list, n) that returns the
# words in word_list shorter than n as a list.
####################################################################################################################

def filter_short_words(word_list, n):
    return filter(lambda word: len(word) < n, word_list)


x = filter_short_words(['aaa', 'dfgdfaw', 'wef', '', 'asdfy', 'df'], 4)
for w in x:
    print(w)

# 3. Write a function that receives any number of strings and returns the list of
# unique strings ordered by number of appearances (most frequent → least frequent).
# f('hello', 'there', 'hello', 'hi', 'hi', 'hello') -> ['hello', 'hi', 'there']
####################################################################################################################

def order_by_appearances(*args):
    return sorted(set(args), key=lambda word: args.count(word), reverse=True)


words = order_by_appearances('mello', 'there', 'mello', 'hi', 'hi', 'mello', 'z', 'z', 'z', 'z')
print(list(words))
