import unittest
from city_functions import full_city_info

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Does function return full info about the city like 'Santiago, Chile'?"""
        city_info = full_city_info('santiago', 'chile')
        self.assertEqual(city_info, 'Santiago, Chile')

    def test_city_country_population(self):
        """Does function return full info about the city like 'Santiago, Chile - 5000000'?"""
        city_info = full_city_info('santiago', 'chile', '5000000')
        self.assertEqual(city_info, 'Santiago, Chile - 5000000')

if __name__ == '__main__':
    unittest.main()
