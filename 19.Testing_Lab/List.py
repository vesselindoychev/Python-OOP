from demos import IntegerList
import unittest


class ListTests(unittest.TestCase):

    def test_add_operation_when_element_is_integer__expect_to_add_element(self):
        integer_list = IntegerList()
        internal_list = integer_list.add(1)
        self.assertEqual([1], internal_list)

    def test_add_operation__when_element_is_not_int__expect_exception(self):
        integer_list = IntegerList()

        with self.assertRaises(ValueError):
            integer_list.add('asd')

    def test_remove_index_operation__expect_to_remove_element_on_proper_index(self):
        pass