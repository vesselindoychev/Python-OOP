from demos import Worker
import unittest


class WorkerTests(unittest.TestCase):
    valid_name = 'Worker'
    valid_salary = 1000
    valid_energy = 100

    def test_init__with_valid_name_salary_and_energy__expect_valid_result(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)

        self.assertEqual(self.valid_name, worker.name)
        self.assertEqual(self.valid_salary, worker.salary)
        self.assertEqual(self.valid_energy, worker.energy)

    def test_rest__when_valid__expect_energy_to_be_incremented(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)

        worker.rest()
        self.assertEqual(self.valid_energy + 1, worker.energy)

    def test_work__when_energy_is_equal_to_0__expect_exception(self):
        worker = Worker(self.valid_name, self.valid_salary, 0)

        with self.assertRaises(Exception) as context:
            worker.work()

        self.assertEqual('Not enough energy.', str(context.exception))

    def test_work__when_energy_is_negative__expect_exception(self):
        worker = Worker(self.valid_name, self.valid_salary, -1)

        with self.assertRaises(Exception) as context:
            worker.work()

        self.assertEqual('Not enough energy.', str(context.exception))

    def test_work__when_energy_is_positive__expect_to_increase_money_by_salary_and_decrease_energy(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        worker.work()
        worker.work()

        self.assertEqual(self.valid_salary * 2, worker.money)
        self.assertEqual(self.valid_energy - 2, worker.energy)

    def test_get_info__when_name_and_money_are_valid__expect_valid_result(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)

        expected_info = f'{self.valid_name} has saved 0 money.'
        actual_info = worker.get_info()
        self.assertEqual(expected_info, actual_info)


if __name__ == '__main__':
    unittest.main()
