import unittest
from city_functions import city_country as ct

class NameTestCase(unittest.TestCase):
    """Test for 'city_functions.py'."""

    def test_city_country(self):
        """Do city countries like 'Manila, Philippines' work?"""
        formatted_cities = ct('manila', 'philippines')
        self.assertEqual(formatted_cities, 'Manila, Philippines')

if __name__ == '__main__':
    unittest.main()