import unittest
from unittest.mock import patch, MagicMock
from testpressurecheck import PressureCheck

class TestPressureCheck(unittest.TestCase):
    def setUp(self) -> None:
        self.pressure_check = PressureCheck()

    def test_initial_bibag_pressure(self):
        self.assertEqual(self.pressure_check.bibag_pressure, 0)

    def test_initial_bibag_pressure_check_time(self):
        self.assertEqual(self.pressure_check.bibag_pressure_check_time, 0)

    def test_bibag_pressure_check_interval(self):
        self.assertEqual(self.pressure_check.bibag_pressure_check_interval, BIBAG_PRESSURE_CHECK_INTERVAL)

    def test_bibag_pressure_limit(self):
        self.assertEqual(self.pressure_check.bibag_pressure_limit, BIBAG_PRESSURE_LIMIT)

    