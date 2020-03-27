import inspect

def dump_args(func):
    """Decorator to print function call details - parameters names and effective values.
    """
    def wrapper(*args, **kwargs):
        func_args = inspect.signature(func).bind(*args, **kwargs).arguments
        func_args_str =  ', '.join('{} = {!r}'.format(*item) for item in func_args.items())
        print(f'{func.__module__}.{func.__qualname__} ( {func_args_str} )')
        return func(*args, **kwargs)
    return wrapper

@dump_args
def test(a, b=4, c='text', *args, **kwargs):
    pass

test(1)
test(1, 3)
test(1, d=5)
test(1, 2, 3, 4, 5, d=6, g=12.9)