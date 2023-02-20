import unittest
from unittest import TestCase
from test_demo import add


class MainTest(TestCase):
    def test_add__when_5_and_2__expect_7(self):
        expected = 7
        actual = add(5, 2)

        self.assertEqual(expected, actual)

    def test_add__when_10_and_5__expect15(self):
        expected = 15
        actual = add(10, 5)

        self.assertEqual(expected, actual)

    def test_add__when_None_and_int__expect_exception(self):
        with self.assertRaises(ValueError) as context:
            pass

if __name__ == '__main__':
    unittest.main()