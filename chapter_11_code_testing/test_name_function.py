import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Does function work with names like 'John Doe'?"""
        formatted_name = get_formatted_name('john', 'doe')
        self.assertEqual(formatted_name, 'John Doe')

    def test_first_last_middel_name(self):
        """Does function work with names like 'Wolfgang Amadeus Mozart'?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()
