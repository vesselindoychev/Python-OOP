class CustomList:
    def __init__(self):
        self.__elements = []

    def append(self, value):
        self.__elements.append(value)
        return self.__elements

    def remove(self, index):
        if index < len(self.__elements):
            result = self.__elements[index]
            self.__elements.remove(self.__elements[index])
            return result
        raise IndexError('Index is out of range')

    def get_index(self, index):
        if index < len(self.__elements):
            return self.__elements[index]
        raise IndexError('Index is out of range')

    def extend(self, iterable):
        [self.__elements.append(x) for x in iterable]
        return self.__elements

    def insert(self, index, value):
        if index < len(self.__elements):
            self.__elements.insert(index, value)
            return self.__elements
        raise IndexError('Index is out of range')

    def pop(self):
        if self.__elements:
            return self.__elements.pop()
        raise ValueError('There are nothing to pop()')

    def clear(self):
        self.__elements = []

    def index(self, index):
        if index < len(self.__elements):
            return self.__elements[index]
        raise IndexError('Index is out of range')

    def count(self, value):
        count = 0
        for x in self.__elements:
            if x == value:
                count += 1
        return count

    def reverse(self):
        return self.__elements[::-1]

    def copy(self):
        copy_elements = self.__elements
        return copy_elements

    def size(self):
        return len(self.__elements)

    def add_first(self, value):
        self.__elements.insert(0, value)

    def dictionize(self):
        dict = {}
        for i in range(0, len(self.__elements) + 1, 2):
            if i == len(self.__elements) - 1:
                dict[self.__elements[i]] = ''
            else:
                if self.__elements[i] not in dict:
                    dict[self.__elements[i]] = self.__elements[i + 1]
                else:
                    dict[self.__elements[i]] += self.__elements[i + 1]
        return dict

    def move(self, amount):
        result = self.__elements[0: amount]
        counter = 0
        index = 0
        while counter < amount:
            self.__elements.remove(self.__elements[index])
            counter += 1
        self.__elements.extend(result)
        return self.__elements

    def sum(self):
        return sum(self.__elements)

    def overbound(self):
        max_value = 0
        for x in self.__elements:
            if x > max_value:
                max_value = x

        return max_value

    def underbound(self):
        min_value = self.__elements[0]
        for x in self.__elements:
            if x < min_value:
                min_value = x

        return min_value