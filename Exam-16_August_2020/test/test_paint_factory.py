import unittest

from Exam_10_April_2021.project import PaintFactory


class TestPainFactory(unittest.TestCase):
    valid_ingredients = ["white", "yellow", "blue", "green", "red"]

    def setUp(self) -> None:
        self.paint_factory = PaintFactory('Name', 10)

    def test_init__with_empty_ingredients(self):
        self.assertEqual('Name', self.paint_factory.name)
        self.assertEqual(10, self.paint_factory.capacity)
        self.assertEqual({}, self.paint_factory.ingredients)
        self.assertEqual(self.valid_ingredients, self.paint_factory.valid_ingredients)

    def test_property_products(self):
        self.assertEqual({}, self.paint_factory.products)

    def test_add_ingredient__when_product_not_in_ingredients__expect_exception(self):
        with self.assertRaises(TypeError) as context:
            self.paint_factory.add_ingredient('one', 10)
        self.assertEqual(f"Ingredient of type {'one'} not allowed in {PaintFactory.__name__}", str(context.exception))

    def test_add_ingredient__when_product_in_ingredients(self):
        self.paint_factory.add_ingredient('white', 2)
        self.assertTrue('white' in self.paint_factory.valid_ingredients)
        self.assertEqual({'white': 2}, self.paint_factory.ingredients)
        self.assertEqual({'white': 2}, self.paint_factory.products)

    def test_add_ingredient__when_quantity_is_over_capacity__expect_exception(self):
        with self.assertRaises(ValueError) as context:
            self.paint_factory.add_ingredient('white', 11)
        self.assertEqual("Not enough space in factory", str(context.exception))

    def test_can_add_method(self):
        valid_value = 10
        not_valid_value = 11
        self.assertEqual(True, self.paint_factory.can_add(valid_value))
        self.assertEqual(False, self.paint_factory.can_add(not_valid_value))

    def test_remove_method__when_product_not_in_ingredients__expect_exception(self):
        with self.assertRaises(KeyError) as context:
            self.paint_factory.remove_ingredient('one', 1)
        self.assertEqual("'No such ingredient in the factory'", str(context.exception))

    def test_remove_method__when_product_in_ingredients_and_quantity_is_valid(self):
        self.paint_factory.add_ingredient('white', 5)
        self.paint_factory.remove_ingredient('white', 5)
        self.assertEqual(0, self.paint_factory.ingredients['white'])
        self.assertEqual({'white': 0}, self.paint_factory.ingredients)
        self.assertEqual({'white': 0}, self.paint_factory.products)

    def test_remove_method__when_product_in_ingredients_and_quantity_bigger_except_exception(self):
        self.paint_factory.add_ingredient('white', 5)
        with self.assertRaises(ValueError) as context:
            self.paint_factory.remove_ingredient('white', 6)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(context.exception))


if __name__ == '__main__':
    unittest.main()
