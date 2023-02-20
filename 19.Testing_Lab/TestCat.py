from demos import Cat

import unittest


class CatTests(unittest.TestCase):
    valid_name = 'Cat'
    valid_size = 0
    valid_fed = False
    valid_sleepy = False

    def test_init__with_valid_name__expect_valid_result(self):
        cat = Cat(self.valid_name)

        self.assertEqual(self.valid_name, cat.name)

    def test_cat_eat__expect_to_increase_size(self):
        cat = Cat(self.valid_name)
        cat.eat()
        self.assertEqual(self.valid_size + 1, cat.size)

    def test_cat_eat__expect_cat_to_be_fed(self):
        cat = Cat(self.valid_name)
        cat.eat()
        self.assertTrue(cat.fed)
        # self.valid_fed = True
        # self.assertEqual(self.valid_fed, cat.fed)

    def test_cat_eat__when_cat_is_fed__expect_exception(self):
        cat = Cat(self.valid_name)
        cat.eat()

        with self.assertRaises(Exception) as context:
            cat.eat()

        self.assertEqual('Already fed.', str(context.exception))

    def test_cat_sleep__when_cat_is_not_fed__expect_exception(self):
        cat = Cat(self.valid_name)

        with self.assertRaises(Exception) as context:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(context.exception))

    def test_cat_sleep__when_cat_have_slept__expect_not_to_be_sleepy(self):
        cat = Cat(self.valid_name)
        cat.eat()
        cat.sleep()
        self.assertFalse(cat.sleepy)


if __name__ == '__main__':
    unittest.main()