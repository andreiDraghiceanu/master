import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Before decorated function call')
        result = func(*args, **kwargs)
        print('After decorated function call')
        return result
    return wrapper


def say_hello(name):
    print(f'Hello, {name}')


@decorator
def say_bye():
    """Returns bye string"""
    return 'Bye bye!'


say_hello = decorator(say_hello)
say_hello('Ana')

bye = say_bye()
print(bye)


