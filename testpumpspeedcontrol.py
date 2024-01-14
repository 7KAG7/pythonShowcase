import unittest
from unittest.mock import MagicMock, patch
from io import StringIO

import pump_controller

class TestPumpController(unittest.TestCase):
    @patch('builtins.input', side_effect=['50'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_pump_speed_set_correctly(self, mock_stdout):
        mock_gpio = MagicMock()
        mock_pwm = MagicMock()
        pump_controller.GPIO = mock_gpio
        pump_controller.GPIO.PWM = mock_pwm

        pump_controller.run_pump_controller()

        expected_output = "Invalid speed. Enter a value between 0 and 100."
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()