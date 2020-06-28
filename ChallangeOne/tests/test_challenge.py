import unittest
from challenge import counter


class EasyTestCase(unittest.TestCase):
    def test_easy_input(self):
        self.assertEqual(counter("Andrei"), 6)

    def test_easy_input_two(self):
        self.assertEqual(counter("Draghiceanu"), 11)


class MediumTestCase(unittest.TestCase):
    def test_medium_input(self):
        self.assertEqual(counter("Mohammad Mahjoub"), 15)

    def test_medium_input_two(self):
        with self.assertRaises(Exception):
            self.assertEqual(counter("Mo?."), 2)


class HardTestCase(unittest.TestCase):
    def test_hard_input(self):
        with self.assertRaises(Exception):
            self.assertEqual(counter(' '), 0)

    def test_hard_input_two(self):
        with self.assertRaises(Exception):
            self.assertEqual(counter(None), 0)


if __name__ == "__main__":
    unittest.main()

