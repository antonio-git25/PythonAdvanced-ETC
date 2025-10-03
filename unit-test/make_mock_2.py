import unittest
from unittest.mock import Mock
import speed


#//////////////////////////
class TestSpeed(unittest.TestCase):
    def test_alert_normal(self):
        speed.get_speed = Mock()
        speed.get_speed.return_value = 70
        self.assertFalse(speed.is_speed_violation())

    def test_alert_overspeed(self):
        speed.get_speed = Mock()
        speed.get_speed.return_value = 100
        self.assertFalse(speed.is_speed_violation())

    def test_alert_underspeed(self):
        speed.get_speed = Mock()
        speed.get_speed.return_value = 59
        self.assertTrue(speed.is_speed_violation())



if __name__ == '__main__':
    unittest.main()


