# decorators


# def hello():
#     print('hellllooooo')
#
#
# greet = hello
# del hello
# print(greet())

# Higher order function HOC


def greet(func):
    func()


def greet2():
    def func():
        return 5
    return func


def my_decorator(func):
    def wrap_function():
        print('*********')
        func()
        print('*********')
    return wrap_function


@my_decorator
def hello():
    print('helllooooo')


@my_decorator
def bye():
    print('see ya later')


hello()
print('')
bye()

