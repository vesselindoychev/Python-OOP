def debug(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        params = []

        if args:
            args_string = ', '.join(str(x) for x in args)
            params.append(args_string)

        if kwargs:
            kwarg_string = ', '.join(f'{key}={value}' for key, value in kwargs.items())
            params.append(kwarg_string)

        params_string = ', '.join(params)

        print(f'{func.__name__}({params_string}) = {result}')

        return result

    return wrapper


@debug
def my_sum(x, y):
    return x + y

@debug
def my_sum_three(x, y, z):
    return x + y + z


print(my_sum(1, y=3))
print(my_sum_three(2, 3, z=4))
