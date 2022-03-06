import unittest
from employee import Employee as emp

class TestEmployee(unittest.TestCase):
    """"Tests for the module Employee"""

    def setUp(self):
        """Make an employee to use in tests"""
        self.rico = emp('rico', 'palomo', 95_000)

    def test_give_default_raise(self):
        """Test a default raise works correctly"""
        self.rico.give_raise()
        self.assertEqual(self.rico.annual_salary, 100000)

    def test_give_custom_raise(self):
        """Test that a custom raise works correctly"""
        self.rico.give_raise(20000)
        self.assertEqual(self.rico.annual_salary, 115000)

if __name__ == '__main__':
    unittest.main()