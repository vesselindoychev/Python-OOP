import functools

from main import log


def uppercase(func):
    @functools.wraps(func)
    def wrapper_uppercase():
        result = func()
        return str(result).upper()

    return wrapper_uppercase


def lowercase(func2):
    functools.wraps(func2)
    def wrapper_lowercase():
        result2 = func2()
        return str(result2).lower()

    return wrapper_lowercase


@log
@uppercase
def say_hi():
    return 'Hello, Doncho!'

@log
@uppercase
def say_bye():
    return 'Bye, Doncho!'


#
# say_hi = uppercase(say_hi)
# say_bye = uppercase(say_bye)

print(say_hi())
print(say_bye())

# say_hi = lowercase(say_hi)
# say_bye = lowercase(say_bye)
#
# print(say_hi())
# print(say_bye())
