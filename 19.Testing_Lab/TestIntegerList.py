import unittest
from demos import IntegerList


class TestList(unittest.TestCase):
    def setUp(self) -> None:
        self.list_integers = IntegerList(1, 2, 3)

    def test_init__with_int_elements(self):
        self.assertEqual([1, 2, 3], self.list_integers._IntegerList__data)

    def test_init__with_non_int_elements(self):
        list_integers = IntegerList("1", 2.1, 3.2)
        self.assertEqual([], list_integers._IntegerList__data)

    def test_add_method__with_int_element__expect_to_be_added(self):
        actual_result = self.list_integers.add(1)
        expected_result = [1, 2, 3, 1]
        self.assertEqual(expected_result, actual_result)

    def test_add_method__with_not_int_element__expect_to_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.list_integers.add(1.2)
        self.assertEqual("Element is not Integer", str(context.exception))

    def test_remove_index__when_index_is_not_in_range__expect_exception(self):
        with self.assertRaises(IndexError) as context:
            self.list_integers.remove_index(4)
        self.assertEqual("Index is out of range", str(context.exception))

    def test_remove_index__when_index_is_in_range__expect_to_be_removed(self):
        result = self.list_integers.remove_index(2)
        self.assertTrue(result not in self.list_integers._IntegerList__data)
        self.assertEqual([1, 2], self.list_integers._IntegerList__data)

    def test_get_method__when_index_is_not_in_range__expect_exception(self):
        with self.assertRaises(IndexError) as context:
            self.list_integers.get(4)
        self.assertEqual("Index is out of range", str(context.exception))

    def test_get_method__when_index_is_in_range__expect_to_be_returned(self):
        result = self.list_integers.get(2)

        self.assertEqual(result, 3)
        self.assertEqual([1, 2, 3], self.list_integers._IntegerList__data)

    def test_insert_method__with_index_out_of_range__expect_exception(self):
        with self.assertRaises(IndexError) as context:
            self.list_integers.insert(3, 1)
        self.assertEqual("Index is out of range", str(context.exception))

    def test_insert_method__with_non_int_element__expect_exception(self):
        with self.assertRaises(ValueError) as context:
            self.list_integers.insert(0, '1')

        self.assertEqual("Element is not Integer", str(context.exception))

    def test_insert_method__with_valid_element_and_index__expect_to_be_inserted(self):
        self.list_integers.insert(0, 10)
        self.assertEqual([10, 1, 2, 3], self.list_integers._IntegerList__data)
        self.assertTrue(10 in self.list_integers._IntegerList__data)

    def test_get_biggest_element(self):
        result = self.list_integers.get_biggest()
        self.assertEqual(3, result)

    def test_get_index(self):
        result = self.list_integers.get_index(1)
        self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()
