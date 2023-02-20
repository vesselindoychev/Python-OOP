from demo_project.customer import Vehicle
import unittest


class TestVehicle(unittest.TestCase):
    fuel = 100
    horse_power = 120

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_vehicle_init__expect_correct_result(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(self.fuel, self.vehicle.capacity)
        self.assertEqual(self.horse_power, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_method__with_not_enough_fuel__expect_exception(self):
        max_distance = self.vehicle.fuel / self.vehicle.fuel_consumption

        with self.assertRaises(Exception) as context:
            self.vehicle.drive(max_distance + 1)

        self.assertEqual("Not enough fuel", str(context.exception))

    def test_drive_method__with_enough_fuel__expect_fuel_to_be_decreased(self):
        max_distance = self.vehicle.fuel / self.vehicle.fuel_consumption

        self.vehicle.drive(max_distance)
        self.assertEqual(0, self.vehicle.fuel)

    def test_refuel_method__with_more_fuel_than_capacity__expect_exception(self):

        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(10)

        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual("Too much fuel", str(context.exception))

    def test_refuel_method__with_enough_fuel__expect_to_increase_fuel(self):
        distance = 10
        self.vehicle.drive(distance)
        consumed_fuel = distance * self.vehicle.fuel_consumption
        recharged_fuel = consumed_fuel / 2
        expected_fuel = self.vehicle.fuel + recharged_fuel

        self.vehicle.refuel(recharged_fuel)
        self.assertEqual(expected_fuel, self.vehicle.fuel)

    def test_str_method__expect_correct_result(self):
        expected_expression = f"The vehicle has {self.horse_power} " \
                              f"horse power with {self.fuel} fuel left and {Vehicle.DEFAULT_FUEL_CONSUMPTION} fuel consumption"

        actual_expression = str(self.vehicle)

        self.assertEqual(expected_expression, actual_expression)


if __name__ == '__main__':
    unittest.main()
