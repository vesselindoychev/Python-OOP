from custom_list import CustomList

custom_list = CustomList()

custom_list.append(1)
custom_list.append(100)
custom_list.append(3)
custom_list.append(3)
print(custom_list.append(10))
custom_list.append(3)

print(custom_list.remove(3))
print(custom_list.get_index(2))
print(custom_list.extend([2, 4, 2, 1, 5]))
print(custom_list.insert(5, 666))
print(custom_list.pop())
print(custom_list.count(3))

print(custom_list.copy())
print(custom_list.append(1))
print(custom_list.copy())
# print(custom_list.clear())
print(custom_list.reverse())
print(custom_list.dictionize())
print(custom_list.move(3))
print(custom_list.sum())
print(custom_list.overbound())
print(custom_list.underbound())