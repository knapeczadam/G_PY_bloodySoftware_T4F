from event_inputs import EventValidator
import unittest


class MyTestCase(unittest.TestCase):

    def test_valid_date_reFALSE(self):
        self.assertFalse(EventValidator.is_valid_date("12a21a"))

    def test_valid_date_reTrue(self):
        self.assertTrue(EventValidator.is_valid_date("2020.10.09"))

    def test_valid_date_reFALSE(self): # par nap mulva mar el fog bukni
        self.assertFalse(EventValidator.is_valid_date("2020.10.10"))

    def test_valid_date_reFALSE(self):
        self.assertFalse(EventValidator.is_valid_date("2015.11.20"))

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

    def test_valid_city_reTRUE(self):
        self.assertTrue(EventValidator.is_valid_city("Miskolc"))

    def test_valid_city_reTRUE(self):
        self.assertTrue(EventValidator.is_valid_city("miskolc"))

    def test_valid_city_reFALSE(self):
        self.assertFalse(EventValidator.is_valid_city("iskolc"))

    def test_valid_address_reTRUE(self):
        self.assertTrue(EventValidator.is_valid_address("a"))

    def test_valid_address_reFALSE(self):
        self.assertFalse(EventValidator.is_valid_address(""))

    def test_valid_address_reFALSE(self):
        self.assertFalse(EventValidator.is_valid_address("11111111111111111111111111"))

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
