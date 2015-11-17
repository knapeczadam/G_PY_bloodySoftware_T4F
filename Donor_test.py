from datetime import datetime
from Donor2 import DonorData

import unittest


class MyTestCase(unittest.TestCase):

    def test_szam_TRUE(self):
        self.assertTrue(DonorData.get_weight(1))

    def test_betu_FALSE(self):
        self.assertFalse(DonorData.get_weight("kk"))

    def test_semmi_TRUE(self):
        self.assertTrue(DonorData.get_weight(""))

    def test_name_reTRUE(self):
        self.assertTrue(DonorData.get_name("Timko And"))

    def test_name_reFALSE(self):
        self.assertFalse(DonorData.get_name("CsakEgy"))

    def test_name_reFALSE(self):
        self.assertFalse(DonorData.get_name(88))

    def test_date_reTRUE(self):
        self.assertTrue(DonorData.get_birth("1996.09.25"))

    def test_date_reFALSE(self):
        self.assertFalse(DonorData.get_birth("1996.xx.25"))

    def test_date_don_reTRUE(self):
        self.assertTrue(DonorData.get_donation("1996.09.25"))

    def test_date_don_reFALSE(self):
        self.assertFalse(DonorData.get_donation("1996.xx.25"))

    def gender_test_reTRUE(self):
        self.assertTrue(DonorData.get_gender("F"))

    def gender_test_reFALSE(self):
        self.assertFalse(DonorData.get_gender("X"))

    def gender_test_reFALSE2(self):
        self.assertFalse(DonorData.get_gender(9))

    def sick_test_reTRUE(self):
        self.assertTrue(DonorData.get_sickness("y"))

    def sick_test_reFALSE(self):
        self.assertFalse(DonorData.get_sickness(9))

    def blood_test_reTRUE(self):
        self.assertTrue(DonorData.get_blood("a"))

    def blood_test_reFALSE(self):
        self.assertFalse(DonorData.get_blood(9))

    def mobil_test_reTRUE(self):
        self.assertTrue(DonorData.get_mobile_number("06202946922"))

    def mobil_test_reFALSE(self):
        self.assertFalse(DonorData.get_mobile_number("062029469"))

    def mobil_test_reFALSE2(self):
        self.assertFalse(DonorData.get_mobile_number("02029469"))

    def mobil_test_reFALSE3(self):
        self.assertFalse(DonorData.get_mobile_number("065029469"))

