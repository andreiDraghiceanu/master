def number_of_appearances(word_list):
    appearances = {}  # dict()
    for word in set(word_list):
        appearances[word] = word_list.count(word)
    return appearances


assert number_of_appearances(['hello', 'hello', 'is', 'there', 'anybody', 'in', 'there']) == \
{'hello': 2, 'is': 1, 'there': 2, 'anybody': 1, 'in': 1}


def map_lists(list1, list2):
    lists_map = {}
    min_len = min(len(list1), len(list2))
    for i in range(min_len):
        lists_map[list1[i]] = list2[i]
    return lists_map


d = map_lists([1, 2, 3, 4], ['a', 'b', 'c'])
print(d)
