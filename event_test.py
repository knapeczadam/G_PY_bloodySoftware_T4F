from event import EventValidator
import unittest


class MyTestCase(unittest.TestCase):

    def test_don_end_reTRUE(self):
        self.assertTrue(EventValidator.is_valid_time("10:10"))

    def test_don_end_reFALSE(self):
        self.assertFalse(EventValidator.is_valid_time("aa:10"))

    def test_zip_code_reTRUE(self):
        self.assertTrue(EventValidator.is_valid_zip_code("1111"))

    def test_zip_code_reFALSE(self):
        self.assertFalse(EventValidator.is_valid_zip_code("0111"))

    def test_zip_code_reFALSE2(self):
        self.assertFalse(EventValidator.is_valid_zip_code("AA11"))

    def test_zip_code_reFALSE3(self):
        self.assertFalse(EventValidator.is_valid_zip_code("AAAAA"))

    def test_planned_donor_True(self):
        self.assertTrue(EventValidator.is_valid_planned_donor_number("100"))

    def test_planned_donor_False(self):
        self.assertFalse(EventValidator.is_valid_planned_donor_number("abc"))

    def test_planned_donor_False2(self):
        self.assertFalse(EventValidator.is_valid_planned_donor_number("abc"))

    def test_available_beds_True(self):
        self.assertTrue(EventValidator.is_valid_available_beds("10"))

    def test_available_beds_False(self):
        self.assertFalse(EventValidator.is_valid_available_beds("abc"))

    def test_succes_rate_False(self):
        self.assertFalse(EventValidator.is_valid_success_rate("abc"))

    def test_succes_rate_False2(self):
        self.assertTrue(EventValidator.is_valid_success_rate("151"))


if __name__ == '__main__':
    unittest.main()
