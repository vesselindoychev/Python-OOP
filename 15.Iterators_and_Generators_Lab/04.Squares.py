# Var2

def squares(n):
    for x in range(1, n + 1):
        yield x * x


print(list(squares(5)))

"""
Var 1
def squares(n):
    return (x * x for x in range(1, n + 1))


print(list(squares(5)))
"""
