def log_decorator(a_function):

    def a_wrapper(*args, **kwargs):
        if len(args) == 0:
            print(f'Running function {a_function.__name__}')
        else:
            a_i = args[0]
            print(f'Running function {a_function.__name__} for {a_i} time(s).')
        a_function()

    return a_wrapper


@log_decorator
def function_a():
    print('I am funtion A.')
    return


@log_decorator
def function_b():
    print('I am function B.')
    return


i = 1
function_b(i)
i += 1
function_a(i)
function_b()
