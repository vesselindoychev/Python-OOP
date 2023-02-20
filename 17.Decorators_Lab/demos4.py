import functools


def repeat(count=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = ''
            for _ in range(count):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat()
def say_hi():
    print('Hi, Doncho!')


say_hi()
