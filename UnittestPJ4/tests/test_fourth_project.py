import time
import unittest
from fourth_project import FibonacciSequence


class TestEfficiency(unittest.TestCase):

    def setUp(self):
        self.fibonacci_sequence = FibonacciSequence()
        self.efficiency_data = dict()

    def test_first_method(self):
        starting_time = time.time()

        self.fibonacci_sequence.recursive_method(32)

        ending_time = time.time()

        self.efficiency_data['recursive_method'] = ending_time - starting_time

    def test_second_method(self):
        starting_time = time.time()

        self.fibonacci_sequence.math_method(600)

        ending_time = time.time()

        self.efficiency_data['math_method'] = ending_time - starting_time

    def tearDown(self):
        print(self.efficiency_data)
        self.fibonacci_sequence = None
        self.efficiency_data.clear()


if __name__ == '__main__':
    unittest.main()

