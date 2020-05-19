A = 100


def func(a):
    c = 5
    global A
    A = 1

    def inner_func(x):
        nonlocal a
        a = 'AAA'
        print('Inside inner func: x=', x,  ', a =', a, ', c =', c, ', A =', A)

    inner_func('some x')
    print('Inside func: a =', a, ', c =', c, ', A =', A)


if __name__ == '__main__':
    func('aaa')
    print('Global scope: A =', A)
    # Cannot call inner_func from global scope
    # func.inner_func()
