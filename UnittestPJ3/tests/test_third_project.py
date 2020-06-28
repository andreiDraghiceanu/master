import sys
import unittest
from third_project import Profile
from io import StringIO


class TestPrintedOutPut(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.profile = Profile("Andrei Draghiceanu", 30, "Automation Engineer")

    def test_name(self):
        self.profile.print_name()
        self.assertEqual(sys.stdout.getvalue(), "Andrei Draghiceanu")

    def test_age(self):
        self.profile.print_age()
        self.assertEqual(sys.stdout.getvalue(), "30")

    def test_job(self):
        self.profile.print_job()
        self.assertEqual(sys.stdout.getvalue(), "Automation Engineer")

    def tearDown(self):
        self.profile = None


if __name__ == '__main__':
    unittest.main()
