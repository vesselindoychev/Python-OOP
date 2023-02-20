import unittest

from Exam_10_April_2021.project import PetShop


class PetShopTests(unittest.TestCase):
    name = 'Name'

    def setUp(self) -> None:
        self.pet_shop = PetShop(self.name)

    def test_pet_shop_init(self):
        self.assertEqual(self.name, self.pet_shop.name)
        self.assertDictEqual({}, self.pet_shop.food)
        self.assertListEqual([], self.pet_shop.pets)

    def test_add_food_method__when_quantity_is_0_or_less__expect_exception(self):
        for quantity in [0, -1]:
            with self.assertRaises(Exception) as context:
                self.pet_shop.add_food('name', quantity)
            self.assertEqual('Quantity cannot be equal to or less than 0', str(context.exception))

    # TODO
    def test_add_food_method__when_name_not_in_foods(self):
        name = 'name'
        quantity = 10
        result = self.pet_shop.add_food(name, quantity)
        self.assertEqual(1, len(self.pet_shop.food))
        self.assertTrue(name in self.pet_shop.food)
        self.assertEqual({name: quantity}, self.pet_shop.food)
        self.assertEqual(quantity, self.pet_shop.food[name])
        self.assertEqual(f"Successfully added {quantity:.2f} grams of {name}.", result)

    def test_add_pet_method__when_name_not_added(self):
        name = 'cat'
        result = self.pet_shop.add_pet(name)
        self.assertTrue(name in self.pet_shop.pets)
        self.assertEqual(f"Successfully added {name}.", result)

    def test_add_pet_method__when_name_is_already_added__expect_exception(self):
        name = 'cat'
        self.pet_shop.add_pet(name)

        with self.assertRaises(Exception) as context:
            self.pet_shop.add_pet(name)
        self.assertEqual("Cannot add a pet with the same name", str(context.exception))

    def test_feed_pet_method__when_pet_is_not_added__expect_exception(self):
        food_name = 'food'
        pet_name = 'name'
        self.pet_shop.add_food(food_name, 5)
        with self.assertRaises(Exception) as context:
            self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual(f"Please insert a valid pet name", str(context.exception))

    def test_feed_pet_method__when_food_is_not_added__expect_exception(self):
        food_name = 'food name'
        pet_name = 'pet name'

        self.pet_shop.add_pet(pet_name)
        result = self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual(f'You do not have {food_name}', result)

    def test_feed_pet_method__when_food_quantity_is_below_100(self):
        food_name = 'food'
        pet_name = 'pet'

        self.pet_shop.add_pet(pet_name)
        self.pet_shop.add_food(food_name, 99)
        self.assertEqual(99, self.pet_shop.food[food_name])
        self.assertTrue(99 < 100)
        result = self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual(1099, self.pet_shop.food[food_name])
        self.assertEqual("Adding food...", result)

    def test_feed_pet_method__when_food_quantity_is_100_and_over(self):
        food_name = 'food'
        pet_name = 'pet'

        self.pet_shop.add_pet(pet_name)
        self.pet_shop.add_food(food_name, 100)
        self.assertEqual(100, self.pet_shop.food[food_name])
        result = self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual(0, self.pet_shop.food[food_name])
        self.assertEqual(f"{pet_name} was successfully fed", result)

    def test_repr_method__when_no_pets(self):
        expected = f'Shop {self.name}:\n'
        expected += f'Pets: '
        actual = repr(self.pet_shop)
        self.assertEqual(expected, actual)

    def test_repr_method__when_have_pets(self):
        self.pet_shop.add_pet('name')
        self.pet_shop.add_pet('name2')

        expected = f'Shop {self.name}:\n'
        expected += f'Pets: {", ".join(self.pet_shop.pets)}'
        actual = repr(self.pet_shop)
        self.assertEqual(expected, actual)
