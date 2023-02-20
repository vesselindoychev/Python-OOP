class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current_number = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_number > self.end:
            raise StopIteration

        value_to_return = self.current_number
        self.current_number += 1

        return value_to_return


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)

# Correct solution
"""class custom_range_iter:
    def __init__(self, custom_range):
        self.custom_range = custom_range
        self.current_number = self.custom_range.start

    def __next__(self):
        if self.current_number > self.custom_range.end:
            raise StopIteration

        value_to_return = self.current_number
        self.current_number += 1

        return value_to_return


class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return custom_range_iter(self)


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
"""
