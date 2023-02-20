import unittest
from unittest import TestCase
from person import Person


class TestDemos(TestCase):
    first_name = 'Test'
    last_name = 'Testov'
    age = 10

    def setUp(self) -> None:
        self.person = Person(self.first_name, self.last_name, self.age)

    def test_person_init__with_valid_names_and_age_expect_to_create_person(self):
        self.assertEqual(self.first_name, self.person.first_name)
        self.assertEqual(self.last_name, self.person.last_name)
        self.assertEqual(self.age, self.person.age)

    def test_get_full_name__with_valid_names_and_age__expect_valid_result(self):
        expected_result = f'{self.first_name} {self.last_name}'
        actual_result = self.person.get_full_name()

        self.assertEqual(expected_result, actual_result)

    def test_get_info__with_valid_names_and_age__expect_valid_info(self):
        expected_info = f'{self.first_name} {self.last_name} is {self.age} years old'
        actual_info = self.person.get_info()

        self.assertEqual(expected_info, actual_info)

    def test_person_init__when_names_are_valid_and_age_is_less_than_min_age__expect_error(self):
        with self.assertRaises(ValueError) as context:
            Person(first_name='Test', last_name='Testov', age=Person.MIN_AGE - 1)
            raise ValueError('Age must be bigger or equal to min age', context.exception)

    def test_person_init__when_names_are_valid_and_age_is_bigger_than_max_age_expct_error(self):
        with self.assertRaises(ValueError) as context:
            Person(first_name='Test', last_name='Testov', age=Person.MAX_AGE + 1)
            raise ValueError('Age must be less or equal to max age', context.exception)


if __name__ == '__main__':
    unittest.main()
