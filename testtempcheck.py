import unittest import TestCase, main 
from unittest.mock import MagicMock
from tempcheck import TempCheck

class TestTempCheck(unittest.TestCase):
    def test_low_temperature_alarm(self):
        temp_check = TempCheck()
        temp_check.current_temp < 20

if __name__ == '__main__':
    unittest.main() 