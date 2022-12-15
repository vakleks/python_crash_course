import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Does function work with names like 'John Doe'?"""
        formatted_name = get_formatted_name('john', 'doe')
        self.assertEqual(formatted_name, 'John Doe')

if __name__ == '__main__':
    unittest.main()

