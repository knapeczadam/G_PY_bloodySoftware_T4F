from _011_donor_inputs import Donor
import unittest


class DonorTests(unittest.TestCase):
	def test_name_with_valid_string(self):
		self.assertTrue(Donor.is_valid_name('david'))

	def test_name_with_string_and_number(self):
		self.assertFalse(Donor.is_valid_name('david0'))

	def test_name_with_spaces(self):
		self.assertFalse(Donor.is_valid_name('       '))

	def test_name_with_empty_string(self):
		self.assertFalse(Donor.is_valid_name(''))

	def test_name_with_one_character(self):
		self.assertFalse(Donor.is_valid_name('d'))

	def test_name_with_two_characters(self):
		self.assertTrue(Donor.is_valid_name('da'))

	def test_weight_with_valid_string(self):
		self.assertTrue(Donor.is_valid_weight('50'))

	def test_weight_with_zero(self):
		self.assertFalse(Donor.is_valid_weight('0'))

	def test_weight_with_letters(self):
		self.assertFalse(Donor.is_valid_weight('abc'))

	def test_weight_with_empty_string(self):
		self.assertFalse(Donor.is_valid_weight(''))

	def test_gender_with_valid_string_lower(self):
		self.assertTrue(Donor.is_valid_gender('f'))

	def test_gender_with_valid_string_upper(self):
		self.assertTrue(Donor.is_valid_gender('F'))

	def test_gender_with_empty_string(self):
		self.assertFalse(Donor.is_valid_gender(''))

	def test_gender_with_number(self):
		self.assertFalse(Donor.is_valid_gender('1'))

	def test_date_with_valid_string(self):
		self.assertTrue(Donor.is_valid_date('2010.01.01'))

	def test_date_with_wrong_date(self):
		self.assertFalse(Donor.is_valid_date('2010.31.01'))

	def test_date_with_letters(self):
		self.assertFalse(Donor.is_valid_date('aaaa.aa.aa'))

	def test_date_with_hyphens(self):
		self.assertFalse(Donor.is_valid_date('2015-06-03'))

	def test_date_with_empty_string(self):
		self.assertFalse(Donor.is_valid_date(''))

	def test_donation_date_with_valid_string(self):
		self.assertTrue(Donor.is_valid_donation_date('2000.01.01'))

	def test_donation_date_with_empty_string(self):
		self.assertTrue(Donor.is_valid_donation_date(''))

	def test_donation_date_with_letters(self):
		self.assertFalse(Donor.is_valid_donation_date('bbbb.bb.bb'))

	def test_donation_date_with_wrong_date(self):
		self.assertFalse(Donor.is_valid_donation_date('2030.30.30'))

	def test_donation_date_with_hyphens(self):
		self.assertFalse(Donor.is_valid_donation_date('2030-02-06'))

	def test_sickness_with_valid_string_lower(self):
		self.assertTrue(Donor.is_valid_sickness('y'))

	def test_sickness_with_valid_string_upper(self):
		self.assertTrue(Donor.is_valid_sickness('N'))

	def test_sickness_with_empty_string(self):
		self.assertFalse(Donor.is_valid_sickness(''))

	def test_sickness_with_number(self):
		self.assertFalse(Donor.is_valid_sickness('2'))

	def test_id_number_with_valid_string(self):
		self.assertTrue(Donor.is_valid_id_number('123456ab'))

	def test_passport_number_with_valid_string(self):
		self.assertTrue(Donor.is_valid_id_number('ab123456'))

	def test_id_number_with_empty_string(self):
		self.assertFalse(Donor.is_valid_id_number(''))

	def test_id_number_with_one_character(self):
		self.assertFalse(Donor.is_valid_id_number('a'))

	def test_id_number_with_nine_characters(self):
		self.assertFalse(Donor.is_valid_id_number('123456abc'))

	def test_id_number_with_eight_hyphens(self):
		self.assertFalse(Donor.is_valid_id_number('--------'))

	def test_id_number_with_spaces(self):
		self.assertFalse(Donor.is_valid_id_number('        '))

	def test_blood_with_valid_string_lower(self):
		self.assertTrue(Donor.is_valid_blood_type('a+'))

	def test_blood_with_valid_string_upper(self):
		self.assertTrue(Donor.is_valid_blood_type('A+'))

	def test_blood_with_empty_string(self):
		self.assertFalse(Donor.is_valid_blood_type(''))

	def test_blood_with_number(self):
		self.assertFalse(Donor.is_valid_blood_type('99'))

	def test_email_with_valid_string_ends_hu(self):
		self.assertTrue(Donor.is_valid_email_address('aaa@bbb.hu'))

	def test_email_with_valid_string_ends_com(self):
		self.assertTrue(Donor.is_valid_email_address('aaa@bbb.com'))

	def test_email_with_wrong_end(self):
		self.assertFalse(Donor.is_valid_email_address('aaa@bbb.de'))

	def test_email_with_two_at_signs(self):
		self.assertFalse(Donor.is_valid_email_address('hello@@world.com'))

	def test_email_with_empty_string(self):
		self.assertFalse(Donor.is_valid_email_address(''))

	def test_email_with_five_characters(self):
		self.assertFalse(Donor.is_valid_email_address('a@.hu'))

	def test_email_with_six_characters(self):
		self.assertTrue(Donor.is_valid_email_address('a@b.hu'))

	def test_email_with_seven_characters(self):
		self.assertTrue(Donor.is_valid_email_address('a@b.com'))

	def test_email_with_spaces(self):
		self.assertFalse(Donor.is_valid_email_address('       '))

	def test_email_with_only_dot_com(self):
		self.assertFalse(Donor.is_valid_email_address('.com@.com....com'))

	def test_email_with_only_dot_hu(self):
		self.assertFalse(Donor.is_valid_email_address('.hu@.hu.hu'))

	def test_email_start_with_dot(self):
		self.assertFalse(Donor.is_valid_email_address('.abc@kkk.com'))

	def test_email_with_dot_before_at_sign(self):
		self.assertFalse(Donor.is_valid_email_address('abc.@kkk.com'))

	def test_mobile_with_06_start_pi_20(self):
		self.assertTrue(Donor.is_valid_mobile_number('06201234567'))

	def test_mobile_with_06_start_pi_30(self):
		self.assertTrue(Donor.is_valid_mobile_number('06301234567'))

	def test_mobile_with_06_start_pi_70(self):
		self.assertTrue(Donor.is_valid_mobile_number('06701234567'))

	def test_mobile_with_36_start_pi_20(self):
		self.assertTrue(Donor.is_valid_mobile_number('+36201234567'))

	def test_mobile_with_36_start_pi_30(self):
		self.assertTrue(Donor.is_valid_mobile_number('+36301234567'))

	def test_mobile_with_36_start_pi_70(self):
		self.assertTrue(Donor.is_valid_mobile_number('+36701234567'))

	def test_mobile_with_wrong_start_var_one(self):
		self.assertFalse(Donor.is_valid_mobile_number('07201234567'))

	def test_mobile_with_wrong_start_var_two(self):
		self.assertFalse(Donor.is_valid_mobile_number('+37201234567'))

	def test_mobile_with_empty_string(self):
		self.assertFalse(Donor.is_valid_mobile_number(''))

	def test_mobile_with_spaces(self):
		self.assertFalse(Donor.is_valid_mobile_number('            '))

	def test_mobile_with_long_len_var_one(self):
		self.assertFalse(Donor.is_valid_mobile_number('+362012345678'))

	def test_mobile_with_long_len_var_two(self):
		self.assertFalse(Donor.is_valid_mobile_number('062012345678'))

	def test_mobile_contains_one_letter_var_one(self):
		self.assertFalse(Donor.is_valid_mobile_number('0620I234567'))

	def test_mobile_contains_one_letter_var_two(self):
		self.assertFalse(Donor.is_valid_mobile_number('+3620I234567'))

if __name__ == '__main__':
	unittest.main()