import unittest
from unittest.mock import patch
import tempcheck

class TestTempCheck(unittest.TestCase):
    @patch('tempcheck.read_temperature_from_controller')
    def test_low_temperature_alarm(self, mock_temp):
        mock_temp.return_value = 19
        with self.assertLogs(level='WARNING') as cm:
            tempcheck.TempCheck.main()
            self.assertTrue(any('Low Temp Alarm' in message for message in cm.output))  

    @patch('tempcheck.read_temperature_from_controller')
    def test_low_temperature_warning(self, mock_temp):
        mock_temp.return_value = 22
        with self.assertLogs(level='WARNING') as cm:
            tempcheck.TempCheck.main()
            self.assertTrue(any('Low Temp Warning' in message for message in cm.output))

    @patch('tempcheck.read_temperature_from_controller')
    def test_low_temperature_shutdown(self, mock_temp):
        mock_temp.return_value = 17
        with self.assertLogs(level='WARNING') as cm:
            tempcheck.TempCheck.main()
            self.assertTrue(any('Low Temp Shutdown' in message for message in cm.output))

    @patch('tempcheck.read_temperature_from_controller')
    def test_high_temperature_alarm(self, mock_temp):
        mock_temp.return_value = 47
        with self.assertLogs(level='WARNING') as cm:
            tempcheck.TempCheck.main()
            self.assertTrue(any('High Temp Alarm' in message for message in cm.output))

    @patch('tempcheck.read_temperature_from_controller')
    def test_high_temperature_warning(self, mock_temp):
        mock_temp.return_value = 44
        with self.assertLogs(level='WARNING') as cm:
            tempcheck.TempCheck.main()
            self.assertTrue(any('High Temp Warning' in message for message in cm.output))

    @patch('tempcheck.read_temperature_from_controller')
    def test_high_temperature_shutdown(self, mock_temp):
        mock_temp.return_value = 49
        with self.assertLogs(level='WARNING') as cm:
            tempcheck.TempCheck.main()
            self.assertTrue(any('High Temp Shutdown' in message for message in cm.output))
                    
if __name__ == '__main__':
    unittest.main() 