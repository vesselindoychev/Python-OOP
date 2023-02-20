class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.index = 0
        self.number = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.count:
            raise StopIteration

        self.index += 1
        self.number += 1
        return self.count - self.number


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
