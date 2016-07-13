import unittest
from converter import RomanNumeralConverter as Converter


class TestRequirements(unittest.TestCase):

    def test_that_tests_are_running(self):
        self.assertEqual(True, True)

    def test_that_converter_returns_i_when_given_1(self):
        self.assertEqual("I", Converter.convert_from_arabic_to_roman(1))

    def test_that_converter_returns_iii_when_given_3(self):
        self.assertEqual("III", Converter.convert_from_arabic_to_roman(3))

    def test_that_converter_returns_ix_when_given_9(self):
        self.assertEqual("IX", Converter.convert_from_arabic_to_roman(9))

    def test_that_converter_returns_mlxvi_when_given_1066(self):
        self.assertEqual("MLXVI", Converter.convert_from_arabic_to_roman(1066))

    def test_that_converter_returns_mcmlxxxix_when_given_1989(self):
        self.assertEqual("MCMLXXXIX", Converter.convert_from_arabic_to_roman(1989))

    def test_that_converter_returns_1_when_given_i(self):
        self.assertEqual(1, Converter.convert_from_roman_to_arabic("I"))

    def test_that_converter_returns_3_when_given_iii(self):
        self.assertEqual(3, Converter.convert_from_roman_to_arabic("III"))

    def test_that_converter_returns_9_when_given_ix(self):
        self.assertEqual(9, Converter.convert_from_roman_to_arabic("IX"))

    def test_that_converter_returns_1066_when_given_mlxvi(self):
        self.assertEqual(1066, Converter.convert_from_roman_to_arabic("MLXVI"))

    def test_that_converter_returns_1989_when_given_mcmlxxxix(self):
        self.assertEqual(1989, Converter.convert_from_roman_to_arabic("MCMLXXXIX"))

if __name__ == '__main__':
    unittest.main()
