# price_list = [('mere', 10), ('pere', 20), ('capsuni', 15)]
# # [('mere', 10*4.75), ('pere', 20*4.75), ...]
#
# out_list = []
# for element in price_list:
#     out_list.append(element[1] * 4.75)
# print(out_list)
#
#
# out_list = []
# for element in price_list:
#     tup = (element[0], element[1] * 4.75)
#     out_list.append(tup)
# print(out_list)
#
#
# out_list = []
# for product, price in price_list:
#     tup = (product, price * 4.75)
#     out_list.append(tup)
# print(out_list)
#
#
# print(list(map(lambda element: element[1] * 4.75, price_list)))
# print(list(map(lambda element: (element[0], element[1] * 4.75), price_list)))
#


def filter_short_words(word_list, n):
    return filter(lambda word: len(word) < n, word_list)


x = filter_short_words(['aaa', 'dfgdfaw', 'wef', '', 'asdfy', 'df'], 4)
for w in x:
    print(w)


def order_by_appearances(*args):
    return sorted(set(args), key=lambda word: args.count(word), reverse=True)


words = order_by_appearances('mello', 'there', 'mello', 'hi', 'hi', 'mello', 'z', 'z', 'z', 'z')
print(list(words))
