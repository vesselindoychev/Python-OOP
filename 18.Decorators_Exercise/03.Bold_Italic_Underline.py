import functools


def make_bold(func):
    @functools.wraps(func)
    def wrapper(*args):
        result = f'<b>{func(*args)}</b>'
        return result

    return wrapper


def make_italic(func):
    @functools.wraps(func)
    def wrapper(*args):
        result = f'<i>{func(*args)}</i>'
        return result

    return wrapper


def make_underline(func):
    @functools.wraps(func)
    def wrapper(*args):
        result = f'<u>{func(*args)}</u>'
        return result

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
