array = [1, 1, 1, 1, 1]
sequence = [1, 1, 1]


def isValidSubsequence(*args):
    for elem in args[1]:
        if args[1].count(elem) > 1:
            if args[1].count(elem) >= args[0].count(elem):
                return False
    if len(args[1]) > len(args[0]):
        return False
    for elem in args[1]:
        if elem not in args[0]:
            return False
    for i in args[1]:
        if i in args[0]:
            return True
        else:
            return False



print(isValidSubsequence(array, sequence))