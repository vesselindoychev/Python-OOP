class reverse_iter:
    def __init__(self, iterable):
        self.iterable = list(iterable)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if abs(self.index) > len(self.iterable):
            raise StopIteration
        value_to_return = self.iterable[self.index]
        self.index -= 1

        return value_to_return


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

# Correct solution
"""class reverse_iter_iterable:
    def __init__(self, reverse_iter):
        self.reverse_iter = reverse_iter
        self.index = -1

    def __next__(self):
        if abs(self.index) > len(self.reverse_iter.iterable):
            raise StopIteration
        value_to_return = self.reverse_iter.iterable[self.index]
        self.index -= 1

        return value_to_return


class reverse_iter:
    def __init__(self, iterable):
        self.iterable = list(iterable)

    def __iter__(self):
        return reverse_iter_iterable(self)


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)"""
