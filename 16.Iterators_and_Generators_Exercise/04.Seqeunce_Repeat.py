class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = list(sequence)
        self.number = number
        self.index = 0
        self.counter = 0

    def __iter__(self):
        return self

    # 1st Var
    def __next__(self):
        if self.counter == self.number:
            raise StopIteration

        if self.index == len(self.sequence):
            self.index = 0

        value_to_return = self.sequence[self.index]
        self.index += 1
        self.counter += 1

        return value_to_return

    # 2nd Var
    # def __next__(self):
    #     if self.index == self.number:
    #         raise StopIteration
    #
    #     value = self.index % len(self.sequence)
    #     value_to_return = self.sequence[value]
    #
    #     self.index += 1
    #
    #     return value_to_return


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
