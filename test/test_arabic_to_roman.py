import unittest
from converter import RomanNumeralConverter as Converter


class TestToRomanConversion(unittest.TestCase):

    def test_that_tests_are_running(self):
        self.assertEqual(True, True)

    def test_that_converter_returns_empty_when_given_0(self):
        self.assertEqual("", Converter.convert_from_arabic_to_roman(0))

    def test_that_converter_returns_i_when_given_1(self):
        self.assertEqual("I", Converter.convert_from_arabic_to_roman(1))

    def test_that_converter_returns_ii_when_given_2(self):
        self.assertEqual("II", Converter.convert_from_arabic_to_roman(2))

    def test_that_converter_returns_iii_when_given_3(self):
        self.assertEqual("III", Converter.convert_from_arabic_to_roman(3))

    def test_that_converter_returns_iv_when_given_4(self):
        self.assertEqual("IV", Converter.convert_from_arabic_to_roman(4))

    def test_that_converter_returns_v_when_given_5(self):
        self.assertEqual("V", Converter.convert_from_arabic_to_roman(5))

    def test_that_converter_returns_vi_when_given_6(self):
        self.assertEqual("VI", Converter.convert_from_arabic_to_roman(6))

    def test_that_converter_returns_vii_when_given_7(self):
        self.assertEqual("VII", Converter.convert_from_arabic_to_roman(7))

    def test_that_converter_returns_ix_when_given_9(self):
        self.assertEqual("IX", Converter.convert_from_arabic_to_roman(9))

    def test_that_converter_returns_x_when_given_10(self):
        self.assertEqual("X", Converter.convert_from_arabic_to_roman(10))

    def test_that_converter_returns_xvi_when_given_16(self):
        self.assertEqual("XVI", Converter.convert_from_arabic_to_roman(16))

    def test_that_converter_returns_l_when_given_50(self):
        self.assertEqual("L", Converter.convert_from_arabic_to_roman(50))

    def test_that_converter_returns_c_when_given_100(self):
        self.assertEqual("C", Converter.convert_from_arabic_to_roman(100))

    def test_that_converter_returns_d_when_given_500(self):
        self.assertEqual("D", Converter.convert_from_arabic_to_roman(500))

    def test_that_converter_returns_m_when_given_1000(self):
        self.assertEqual("M", Converter.convert_from_arabic_to_roman(1000))

    def test_that_converter_returns_mlxvi_when_given_1066(self):
        self.assertEqual("MLXVI", Converter.convert_from_arabic_to_roman(1066))

    def test_that_converter_returns_mcmlxxxix_when_given_1989(self):
        self.assertEqual("MCMLXXXIX", Converter.convert_from_arabic_to_roman(1989))

    def test_that_converter_returns_d_when_given_2494(self):
        self.assertEqual("MMCDXCIV", Converter.convert_from_arabic_to_roman(2494))


if __name__ == '__main__':
    unittest.main()
