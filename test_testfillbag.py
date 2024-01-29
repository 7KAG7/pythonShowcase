import unittest

class PressureCheckTest(unittest.TestCase):
    def test_fill_bibag(self):
        pressure_check = PressureCheck()

        # Test case 1: bibag_pressure < bibag_pressure_limit
        requested_volume = 100
        bibag_volume = 200
        bibag_pressure = 50
        bibag_pressure_limit = 100
        expected_result = bibag_volume + requested_volume
        self.assertEqual(pressure_check.fill_bibag(requested_volume, bibag_volume, bibag_pressure, bibag_pressure_limit), expected_result)

        # Test case 2: bibag_pressure >= bibag_pressure_limit
        requested_volume = 100
        bibag_volume = 200
        bibag_pressure = 150
        bibag_pressure_limit = 100
        expected_result = bibag_volume
        self.assertEqual(pressure_check.fill_bibag(requested_volume, bibag_volume, bibag_pressure, bibag_pressure_limit), expected_result)

if __name__ == '__main__':
    unittest.main()