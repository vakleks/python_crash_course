import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for employee module."""

    def setUp(self):
        """Create an employee for tests."""
        self.johndoe = Employee('John', 'Doe', 20000)

    def test_give_default_raise(self):
        """Test for the default salary raise."""
        self.johndoe.give_raise()
        self.assertEqual(self.johndoe.salary, 25000)

    def test_give_custom_raise(self):
        """Test for the custom salary raise."""
        self.johndoe.give_raise(10000)
        self.assertEqual(self.johndoe.salary, 30000)

if __name__ == '__main__':
    unittest.main()
