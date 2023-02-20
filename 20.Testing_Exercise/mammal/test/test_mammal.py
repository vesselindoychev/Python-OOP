from demo_project.customer import Mammal
import unittest


class TestMammal(unittest.TestCase):
    name = 'Mammal'
    mammal_type = 'type'
    sound = 'sound'

    def setUp(self) -> None:
        self.mammal = Mammal(self.name, self.mammal_type, self.sound)

    def test_init__with_valid_names_type_and_sound__expect_correct_result(self):
        self.assertEqual(self.name, self.mammal.name)
        self.assertEqual(self.mammal_type, self.mammal.type)
        self.assertEqual(self.sound, self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound__with_valid_name_and_sound__expect_correct_sound(self):
        expected_sound = f"{self.name} makes {self.sound}"
        actual_sound = self.mammal.make_sound()

        self.assertEqual(expected_sound, actual_sound)

    def test_kingdom__expect_correct_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_get_info__with_valid_name_and_type_expect_correct_result(self):
        expected_info = f"{self.name} is of type {self.mammal_type}"
        actual_info = self.mammal.info()

        self.assertEqual(expected_info, actual_info)


if __name__ == '__main__':
    unittest.main()
