from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} sec')
        return result
    return wrapper()

# generator performance
@performance
def long_time():
    print('1')
    for i in range(100000000):
        i*5

# list performance
@performance
def long_time2():
    print('2')
    for i in list(range(100000000)):
        i*5

