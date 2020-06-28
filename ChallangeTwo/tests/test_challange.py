import unittest
from challenge import Car


class EasyTestCases(unittest.TestCase):

    def setUp(self):
        self.car = Car()
        self.car.start_car()

    def test_easy_input(self):
        self.assertEqual(self.car.current_speed(), 0)

    def test_easy_input_two(self):
        self.car.start_car()
        self.assertEqual(self.car.car_status(), True)

    def test_easy_input_three(self):
        self.car.stop()
        self.assertEqual(self.car.car_status(), True)

    def tearDown(self):
        self.car.stop()
        self.car.turn_off_car()
        self.car = None


class MediumTestCases(unittest.TestCase):

    def setUp(self):
        self.car = Car()
        self.car.start_car()

    def test_medium_input(self):
        self.car.start_car()
        self.car.add_speed()
        self.car.add_speed()
        self.car.add_speed()
        self.assertEqual(self.car.current_speed(), 15)

    def test_medium_input_two(self):
        self.car.add_speed()
        self.car.add_speed()
        self.car.add_speed()
        self.car.add_speed()
        self.car.remove_speed()
        self.assertEqual(self.car.current_speed(), 15)

    def test_medium_input_three(self):
        self.car.remove_speed()
        self.car.remove_speed()
        self.assertEqual(self.car.current_speed(), 0)

    def test_medium_input_four(self):
        with self.assertRaises(Exception):
            self.car.start_car()

    def test_medium_input_five(self):
        self.car.remove_speed()
        self.car.remove_speed()
        self.car.remove_speed()
        self.car.remove_speed()
        self.assertEqual(self.car.current_speed(), 0)

    def tearDown(self):
        self.car.stop()
        self.car.turn_off_car()
        self.car = None


class HardTestCases(unittest.TestCase):

    def setUp(self):
        self.car = Car()
        self.car.start_car()

    def test_hard_input(self):
        for _ in range(150):
            self.car.add_speed()
        self.assertEqual(self.car.current_speed(), 240)

    def test_hard_input_two(self):
        for _ in range(150):
            self.car.add_speed()
        self.car.stop()
        self.assertEqual(self.car.current_speed(), 0)

    def test_hard_input_three(self):
        for _ in range(150):
            self.car.add_speed()
        self.car.stop()
        self.assertEqual(self.car.car_status(), True)

    def tearDown(self):
        self.car.stop()
        self.car.turn_off_car()
        self.car = None


if __name__ == '__main__':
    unittest.main()
