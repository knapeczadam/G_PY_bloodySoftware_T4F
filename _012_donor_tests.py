from _011_donor_inputs import Donor
import unittest


class MyTestCase(unittest.TestCase):
    def test_szam_TRUE(self):
        self.assertTrue(Donor.is_valid_name("k k"))

    def test_szam_False(self):
        self.assertFalse(Donor.is_valid_name("1"))

    def test_szam_TRUE(self):
        self.assertTrue(Donor.is_valid_weight(1))

    def test_betu_FALSE(self):
        self.assertFalse(Donor.is_valid_weight("kk"))

    def test_semmi_FALSE(self):
        self.assertFalse(Donor.is_valid_weight(""))

    def test_name_reTRUE(self):
            self.assertTrue(Donor.is_valid_name("Timko"))

    def test_name_reFALSE(self):
        self.assertTrue(Donor.is_valid_name("CsakEgy"))

    def test_name_reFALSE2(self):
        self.assertFalse(Donor.is_valid_name("88"))

    def test_date_reTRUE(self):
        self.assertTrue(Donor.is_valid_date("1996.09.25"))

    def test_date_reFALSE(self):
        self.assertFalse(Donor.is_valid_date("1996.xx.25"))

    def test_date_don_reTRUE(self):
        self.assertTrue(Donor.is_valid_donation_date(""))

    def gender_test_reTRUE(self):
        self.assertTrue(Donor.is_valid_gender("F"))

    def gender_test_reFALSE(self):
        self.assertFalse(Donor.is_valid_gender("X"))

    def gender_test_reFALSE2(self):
        self.assertFalse(Donor.is_valid_gender(9))

    def sick_test_reTRUE(self):
        self.assertTrue(Donor.is_valid_sickness("y"))

    def sick_test_reFALSE(self):
        self.assertFalse(Donor.is_valid_sickness(9))

    def blood_test_reTRUE(self):
        self.assertTrue(Donor.is_valid_blood_type("a"))

    def blood_test_reFALSE(self):
        self.assertFalse(Donor.is_valid_blood_type(9))

    def mobil_test_reTRUE(self):
        self.assertTrue(Donor.is_valid_mobile_number("06202946922"))

    def mobil_test_reFALSE(self):
        self.assertFalse(Donor.is_valid_mobile_number("062029469"))

    def mobil_test_reFALSE2(self):
        self.assertFalse(Donor.is_valid_mobile_number("02029469"))

    def mobil_test_reFALSE3(self):
        self.assertFalse(Donor.is_valid_mobile_number("065029469"))

    def email_test_reTRUE(self):
        self.assertTrue(Donor.is_valid_email_address("aaandris@gmail.com"))

    def email_test_reFALSE(self):
        self.assertFalse(Donor.is_valid_email_address("aaandris@gmail"))

    def email_test_reFALSE2(self):
        self.assertFalse(Donor.is_valid_email_address("aaandris.hu"))

    def id_test_reTRUE(self):
        self.assertTrue(Donor.is_valid_id_number("201001AA"))

    def id_test_reTRUE2(self):
        self.assertTrue(Donor.is_valid_id_number("AAAAAA22"))

    def id_test_reTRUE3(self):
        self.assertTrue(Donor.is_valid_id_number("AAAAA322"))

    def id_test_reFALSE(self):
        self.assertFalse(Donor.is_valid_id_number("XXXXXXX"))

