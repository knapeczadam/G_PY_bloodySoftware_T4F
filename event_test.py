from event import EventDataValidator
import unittest


class MyTestCase(unittest.TestCase):
    def test_planned_donor_True(self):
        self.assertTrue(EventDataValidator.is_valid_planned_donor_number("100"))

    def test_planned_donor_False(self):
        self.assertFalse(EventDataValidator.is_valid_planned_donor_number("101"))

    def test_planned_donor_False2(self):
        self.assertFalse(EventDataValidator.is_valid_planned_donor_number("abc"))

    def test_available_beds_True(self):
        self.assertTrue(EventDataValidator.is_valid_available_beds("10"))

    def test_available_beds_False(self):
        self.assertFalse(EventDataValidator.is_valid_available_beds("abc"))

    def test_succes_rate_False(self):
        self.assertFalse(EventDataValidator.is_valid_success_rate("abc"))

    def test_succes_rate_False(self):
        self.assertTrue(EventDataValidator.is_valid_success_rate("151"))


if __name__ == '__main__':
    unittest.main()
