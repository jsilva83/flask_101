import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(a_function):
    def a_wrapper():
        print(f'Start: {time.time()}')
        a_function()
        print(f'End: {time.time()}')

    return a_wrapper


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()