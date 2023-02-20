from Exam_10_April_2021.project import Bakery

# from Exam-21_December_2021-EXAM.table.table import Table

# cake = Cake('Torta', 3.4)
# bread = Bread('Hlebche', 1.5)
# print(cake)
# print(bread)
#
# drink = Tea('Water', 0.25, 'Mihalkovo')
# water = Water('Tea', 0.25, 'Lord Nelson')
# print(drink)
# print(water)

# table = Table(21, 10)
# table.reserve(7)
# table.order_food(bread)
# table.order_drink(water)
# print(table.get_bill())
# table.clear()

bakery = Bakery('BAKERY')
print(bakery.add_food('Bread', 'Franzela', 1.5))
print(bakery.add_food('Bread', 'Topal', 2.5))
print(bakery.add_food('Bread', 'Pulnozurnest', 1.3))
print(bakery.add_food('Bread', 'Bql', 4.5))
print(bakery.add_drink('Tea', 'Chai', 0.12, 'Lord Nelson'))
print(bakery.add_drink('Water', 'Voda', 0.5, 'Bankia'))
print(bakery.add_drink('Water', 'Vodka', 0.75, 'Gorna Bania'))
print(bakery.add_drink('Water', 'Cola', 0.25, 'Coca Cola'))
print(bakery.add_table('InsideTable', 21, 20))
print(bakery.add_table('InsideTable', 1, 4))
print(bakery.reserve_table(10))
print(bakery.reserve_table(2))

print(bakery.order_drink(21, 'Franzela', 'Topal', 'Bql', 'Bageta'))
print(bakery.order_drink(2, 'Franzela', 'Topal', 'Bql', 'Bageta'))

print(bakery.order_drink(1, 'Voda', 'Cola', 'Chai', 'Tea', 'Fanta'))
print(bakery.leave_table(21))
print(bakery.leave_table(1))
print(bakery.get_free_tables_info())
print(bakery.get_total_income())