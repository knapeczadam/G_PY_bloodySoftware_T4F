from _021_event_inputs import Event
import unittest


class EventTests(unittest.TestCase):
    def test_date_of_event_with_valid_string(self):
        self.assertTrue(Event.is_valid_date_of_event("2015.12.24"))

    def test_date_of_event_with_saturday(self):
        self.assertFalse(Event.is_valid_date_of_event("2015.12.26"))

    def test_date_of_event_with_sunday(self):
        self.assertFalse(Event.is_valid_date_of_event("2015.12.27"))

    def test_date_of_event_less_then_ten_days(self):
        self.assertFalse(Event.is_valid_date_of_event("2015.1.27"))

    def test_date_of_event_with_hyphens(self):
        self.assertFalse(Event.is_valid_date_of_event("2015-12-24"))

    def test_date_of_event_contains_letters(self):
        self.assertFalse(Event.is_valid_date_of_event("2O15.I2.24"))

    def test_start_time_with_valid_string(self):
        self.assertTrue(Event.is_valid_start_time("10:10"))

    def test_start_time_with_wrong_time(self):
        self.assertFalse(Event.is_valid_start_time("99:10"))

    def test_start_time_contains_letter(self):
        self.assertFalse(Event.is_valid_start_time("10:1O"))

    def test_start_time_contains_hyphens(self):
        self.assertFalse(Event.is_valid_start_time("10-55"))

    def test_start_time_with_empty_string(self):
        self.assertFalse(Event.is_valid_start_time(""))

    def test_zip_code_with_valid_string(self):
        self.assertTrue(Event.is_valid_zip_code("1111"))

    def test_zip_code_contains_letter(self):
        self.assertFalse(Event.is_valid_zip_code("11I1"))

    def test_zip_code_starts_with_0(self):
        self.assertFalse(Event.is_valid_zip_code("0123"))

    def test_zip_code_contains_five_numbers(self):
        self.assertFalse(Event.is_valid_zip_code("12345"))

    def test_zip_code_with_empty_string(self):
        self.assertFalse(Event.is_valid_zip_code(""))

    def test_city_with_valid_string(self):
        self.assertTrue(Event.is_valid_city("Miskolc"))

    def test_city_with_wrong_string(self):
        self.assertFalse(Event.is_valid_city("iskolc"))

    def test_city_with_upper(self):
        self.assertTrue(Event.is_valid_city("MISKOLC"))

    def test_city_with_lower(self):
        self.assertTrue(Event.is_valid_city("miskolc"))

    def test_city_contains_letter(self):
        self.assertFalse(Event.is_valid_city("misk0lc"))

    def test_city_with_empty_string(self):
        self.assertFalse(Event.is_valid_city(""))

    def test_address_with_valid_string(self):
        self.assertTrue(Event.is_valid_address("a"))

    def test_address_with_empty_string(self):
        self.assertFalse(Event.is_valid_address(""))

    def test_address_with_26_char(self):
        self.assertFalse(Event.is_valid_address("kf hi v9pg,.< v25960KJH f6"))

    def test_available_beds_with_valid_string(self):
        self.assertTrue(Event.is_valid_available_beds("10"))

    def test_available_beds_with_letters(self):
        self.assertFalse(Event.is_valid_available_beds("IO"))

    def test_available_beds_with_empty_string(self):
        self.assertFalse(Event.is_valid_available_beds(""))

    def test_successful_donations_with_valid_string(self):
        self.assertTrue(Event.is_valid_successful_donations("666"))

    def test_successful_donations_with_letters(self):
        self.assertFalse(Event.is_valid_successful_donations("GGG"))

    def test_successful_donations_with_empty_string(self):
        self.assertFalse(Event.is_valid_successful_donations(""))

if __name__ == '__main__':
    unittest.main()
