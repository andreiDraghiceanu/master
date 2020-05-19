def func(date_start, date_end, *args, year=2000, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))

    print(*args)  # print(args[0], args[1], ...)
    # print(**kwargs)  # print(name='Ana', age=20)

    if len(args) > 0:
        first_arg = args[0]

    name = kwargs.get('name', 'Unknown')
    print('Name is', name)

    for arg in args:
        print(arg)

    for arg_name, arg_value in kwargs.items():
        print(arg_name, arg_value)

    print()

func(1, 2, 3)  # positional arguments
# func(name='Ana', age=20)  # keyword arguments
func(1, 2, 3, name='Ana')
func([1, 3], [234, 5765], {'a': 100})
