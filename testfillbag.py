import unittest
from pressurecheck import PressureCheck

class TestPressureCheck(unittest.TestCase):
    def setUp(self):
        self.pressure_check = PressureCheck()

    def test_fill_bibag(self):
        # Test when bibag_pressure is less than bibag_pressure_limit
        self.assertEqual(self.pressure_check.fill_bibag(10, 50, 70, 100), 60)

        # Test when bibag_pressure is equal to bibag_pressure_limit
        self.assertEqual(self.pressure_check.fill_bibag(10, 50, 100, 100), 50)

        # Test when bibag_pressure is more than bibag_pressure_limit
        self.assertEqual(self.pressure_check.fill_bibag(10, 50, 110, 100), 50)

if __name__ == '__main__':
    unittest.main()