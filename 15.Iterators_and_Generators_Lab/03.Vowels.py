class vowels:
    def __init__(self, iterable):
        self.iterable = list(iterable)
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.iterable):
            if self.iterable[self.index].lower() in self.vowels:
                value_to_return = self.iterable[self.index]
                self.index += 1
                return value_to_return
            self.index += 1
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

# Correct solution
"""
class vowels_iter:
    def __init__(self, vowels):
        self.vowels = vowels
        self.alphabetical_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        self.index = 0

    def __next__(self):
        while self.index < len(self.vowels.iterable):
            if self.vowels.iterable[self.index].lower() in self.alphabetical_vowels:
                value_to_return = self.vowels.iterable[self.index]
                self.index += 1
                return value_to_return
            self.index += 1
        raise StopIteration


class vowels:
    def __init__(self, iterable):
        self.iterable = list(iterable)

    def __iter__(self):
        return vowels_iter(self)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

"""
