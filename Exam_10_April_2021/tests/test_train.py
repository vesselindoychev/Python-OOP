import unittest

from project.train.train import Train


class TestTrain(unittest.TestCase):
    TRAIN_FULL = "Train is full"
    PASSENGER_EXISTS = "Passenger {} Exists"
    PASSENGER_NOT_FOUND = "Passenger Not Found"
    PASSENGER_ADD = "Added passenger {}"
    PASSENGER_REMOVED = "Removed {}"
    ZERO_CAPACITY = 0

    name = 'Name'
    capacity = 2

    def setUp(self) -> None:
        self.train = Train(self.name, self.capacity)

    def test_train_init(self):
        self.assertEqual(self.name, self.train.name)
        self.assertEqual(self.capacity, self.train.capacity)
        self.assertEqual([], self.train.passengers)
        self.assertEqual(self.TRAIN_FULL, self.train.TRAIN_FULL)
        self.assertEqual(self.PASSENGER_EXISTS, self.train.PASSENGER_EXISTS)
        self.assertEqual(self.PASSENGER_NOT_FOUND, self.train.PASSENGER_NOT_FOUND)
        self.assertEqual(self.PASSENGER_ADD, self.train.PASSENGER_ADD)
        self.assertEqual(self.PASSENGER_REMOVED, self.train.PASSENGER_REMOVED)
        self.assertEqual(self.ZERO_CAPACITY, self.train.ZERO_CAPACITY)

    def test_add__when_no_capacity__expect_exception(self):
        self.train.add('Ivan')
        self.train.add('Misho')
        with self.assertRaises(ValueError) as context:
            self.train.add('Koko')
        self.assertEqual(self.TRAIN_FULL, str(context.exception))

    def test_add__when_no_passenger_added__expect_exception(self):
        self.train.add('Ivan')
        with self.assertRaises(ValueError) as context:
            self.train.add('Ivan')
        self.assertEqual(self.PASSENGER_EXISTS.format('Ivan'), str(context.exception))

    def test_add_method(self):
        result = self.train.add('Ivan')
        self.assertEqual(['Ivan'], self.train.passengers)
        self.assertEqual(self.PASSENGER_ADD.format('Ivan'), result)
        self.assertTrue('Ivan' in self.train.passengers)

    def test_remove__when_passenger_is_not_in__expect_exception(self):
        with self.assertRaises(ValueError) as context:
            self.train.remove('Ivan')
        self.assertEqual(self.PASSENGER_NOT_FOUND.format('Ivan'), str(context.exception))

    def test_remove__when_passenger_is_in(self):
        self.train.add('Ivan')
        self.train.add('Peter')
        result = self.train.remove('Ivan')
        self.assertEqual(['Peter'], self.train.passengers)
        self.assertEqual(1, len(self.train.passengers))
        self.assertTrue('Ivan' not in self.train.passengers)
        self.assertEqual(self.PASSENGER_REMOVED.format('Ivan'), result)


if __name__ == '__main__':
    unittest.main()
