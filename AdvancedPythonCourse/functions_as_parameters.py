def two_number_sum(a, b):
    return a + b


def two_number_diff(a, b):
    return a - b


def get_result(a, b, operation):
    print(a)
    print(b)
    print(operation)

    print(operation is two_number_sum)
    print(operation is two_number_diff)

    return operation(a, b)


s = get_result(5, 2, two_number_sum)
d = get_result(5, 2, two_number_diff)

print(s, d)
