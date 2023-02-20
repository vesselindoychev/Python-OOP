class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.index = 0
        self.number_of_counts = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number_of_counts == self.count:
            raise StopIteration
        value_to_return = self.index
        self.index += self.step
        self.number_of_counts += 1
        return value_to_return


numbers = take_skip(10, 5)
for number in numbers:
    print(number)

