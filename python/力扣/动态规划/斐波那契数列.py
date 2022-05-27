'''递归'''

import time


# 装饰器
def coast_time(func):
    def fun(*args, **kwargs):
        t = time.perf_counter()
        result = func(*args, **kwargs)
        print(f'func {func.__name__} coast time:{time.perf_counter() - t:.8f} s')
        return result

    return fun


d = {}


def FB(n):
    if n in d.keys():
        return d.get(n)
    if n <= 2:
        return 1
    # return FB(n - 1) + FB(n - 2)
    result = FB(n - 1) + FB(n - 2)
    d[n] = result
    return result

def FB1(n):
    if n <= 2:
        return 1
    return FB(n - 1) + FB(n - 2)


@coast_time
def get_10():
    for i in range(1, 50):
        print(FB(i))

@coast_time
def get_101():
    for i in range(1, 50):
        print(FB1(i))

get_10()
get_101()