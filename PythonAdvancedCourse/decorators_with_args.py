def multiply(nr):
    def multiply_decorator(func):
        def func_wrapper(*arg, **kwargs):
            return nr * func(*arg, **kwargs)
        return func_wrapper
    return multiply_decorator


@multiply(2)
def double_val(val):
    print("Double value " + str(val))
    return val


@multiply(3)
def triple_val(val):
    print("Triple value " + str(val))
    return val


# double_val = multiply(2)(double_val)
# double_val = multiply.<locals>.multiply_decorator(double_val)

print(double_val(10))
print(triple_val(10))
