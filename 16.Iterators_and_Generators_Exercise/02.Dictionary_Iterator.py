class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = list(self.dictionary.keys())
        self.key = 0
        self.value = 0
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.dictionary):
            raise StopIteration

        value_to_return = self.index

        self.key = self.keys[value_to_return]
        self.value = self.dictionary[self.key]

        self.index += 1

        return self.key, self.value


result = dictionary_iter({1: "1", 2: "2", "name": 'Peter'})
for x in result:
    print(x)
