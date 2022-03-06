from city_functions_population import city_country_population as ccp
import unittest

class NameTestCase(unittest.TestCase):
    """Test for 'city_functions_population.py'."""

    def test_city_country(self):
        """Do city countries like 'Bgc, Philippines' work?"""
        formatted_cities = ccp('bgc', 'philippines')
        self.assertEqual(formatted_cities, 'Bgc, Philippines')

    def test_city_country_population(self):
        """Do city countries with population like 'Bgc, Philippines - population 11739' work?"""
        formatted_cities = ccp('bgc', 'philippines', '11739')
        self.assertEqual(formatted_cities, 'Bgc, Philippines - population 11739')

if __name__ == '__main__':
    unittest.main()
