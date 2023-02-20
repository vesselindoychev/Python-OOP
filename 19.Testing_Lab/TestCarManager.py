import unittest



class TestCar(unittest.TestCase):
    make = 'Car'
    model = 'Model'
    fuel_consumption = 6.5
    fuel_capacity = 100

    def setUp(self) -> None:
        self.car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

    def test_car_init(self):
        self.assertEqual(self.fuel_capacity, self.car.fuel_capacity)
        self.assertEqual(self.fuel_consumption, self.car.fuel_consumption)
        self.assertEqual(self.make, self.car.make)
        self.assertEqual(self.model, self.car.model)

    def test_make_method__when_empty_or_null__expect_exception(self):
        for make in [0, '']:
            with self.assertRaises(Exception) as context:
                self.car.make = make
            self.assertEqual("Make cannot be null or empty!", str(context.exception))

    def test_make_method__with_valid_element(self):
        self.car.make = 'Car makes make'
        self.assertEqual('Car makes make', self.car.make)

    def test_model__when_it_is_empty_or_0__expect_exception(self):
        for model in [0, '']:
            with self.assertRaises(Exception) as context:
                self.car.model = model
            self.assertEqual("Model cannot be null or empty!", str(context.exception))

    def test_model__with_valid_model__expect_to_be_set(self):
        self.car.model = 'New Model'
        self.assertEqual('New Model', self.car.model)

    def test_fuel_consumption__when_it_is_0_or_less__expect_exception(self):
        for fuel_consumption in [0, -10]:
            with self.assertRaises(Exception) as context:
                self.car.fuel_consumption = fuel_consumption
            self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))

    def test_fuel_consumption__when_it_is_valid(self):
        self.car.fuel_consumption = 10
        self.assertEqual(10, self.car.fuel_consumption)

    def test_fuel_capacity__when_it_is_0_or_less_expect_exception(self):
        for fuel_capacity in [0, -1]:
            with self.assertRaises(Exception) as context:
                self.car.fuel_capacity = fuel_capacity
            self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))

    def test_fuel_capacity__when_it_is_bigger_than_0(self):
        self.car.fuel_capacity = 60
        self.assertEqual(60, self.car.fuel_capacity)

    def test_fuel_amount__when_it_is_less_than_0__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(context.exception))

    def test_fuel_amount__when_it_is_valid(self):
        self.car.fuel_amount = 30
        self.assertEqual(30, self.car.fuel_amount)

    def test_refuel_method__when_fuel_is_0_or_less_expect_exception(self):
        for fuel in [0, -1]:
            with self.assertRaises(Exception) as context:
                self.car.refuel(fuel)
            self.assertEqual("Fuel amount cannot be zero or negative!", str(context.exception))

    def test_refuel_method__when_fuel_is_valid(self):
        fuel = 30
        self.car.refuel(fuel)

        self.assertEqual(fuel, self.car.fuel_amount)

    def test_refuel_method__when_fuel_amount_is_bigger_than_capacity__expect__fuel_amount_to_be_equal_to_capacity(self):
        self.car.refuel(self.fuel_capacity + 1)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_drive__when_there_is_no_fuel(self):
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as context:
            self.car.drive(10)
        self.assertEqual("You don't have enough fuel to drive!", str(context.exception))

    def test_drive__when_there_is_enough_fuel(self):
        self.car.refuel(100)
        self.assertEqual(100, self.car.fuel_amount)
        self.car.drive(10)
        self.assertEqual(99.35, self.car.fuel_amount)

    def test_drive_without_enough_fuel_expect_exception(self):
        self.car.refuel(0.1)
        with self.assertRaises(Exception) as context:
            self.car.drive(50)
        self.assertEqual("You don't have enough fuel to drive!", str(context.exception))


if __name__ == '__main__':
    unittest.main()
