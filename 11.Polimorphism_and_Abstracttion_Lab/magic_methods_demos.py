class Items:
    def __init__(self, *args):
        self.items = list(args)
        self.count = 0

    def add_item(self, value):
        self.items.append(value)
        self.count += 1

    def __str__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        result = Items()
        [result.add_item(x) for x in self.items]
        [result.add_item(x) for x in other.items]
        return result

    def __sub__(self, other):
        result2 = Items()
        [result2.add_item(x) for x in self.items]
        [result2.add_item(x) for x in other.items]
        return result2

    def __mul__(self, other):
        result3 = Items()
        [result3.add_item(x) for x in self.items * other]
        return result3

    # def __eq__(self, other):
    #     return self.items == other.items


# ii = Items()
# ii.add_item(1)
# ii.add_item(2)
#
# ii2 = Items()
# ii2.add_item(-1)
# print(len(ii))
# print(len(ii2))
#
# print(ii + ii2)
#
# print(len(ii) + len(ii2))
#
# print(len(ii) - len(ii2))
#
# print(ii * 2)
# print(ii2 * 2)

i1 = Items(1, 2, 3)
i2 = Items(-1)
i3 = Items(10, 12)

print(Items(1, 2, 3) == Items(1, 2, 3))
print([1, 2, 3] == [1, 2, 3])
print(i1 != i2)

class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary

p1 = Person('Ivan', 1200)
p2 = Person('Gosho', 800)
p3 = Person('Petar', 4000)
print(p1 > p2)
print(p1 > p3)

