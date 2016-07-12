import unittest
from converter import RomanNumeralConverter as Converter


class TestToArabicConversion(unittest.TestCase):

    def test_that_tests_are_running(self):
        self.assertEqual(True, True)

    def test_that_converter_returns_1_when_given_i(self):
        self.assertEqual(1, Converter.convert_from_roman_to_arabic("I"))

    def test_that_converter_returns_5_when_given_v(self):
        self.assertEqual(5, Converter.convert_from_roman_to_arabic("V"))

    def test_that_converter_returns_30_when_given_xxx(self):
        self.assertEqual(30, Converter.convert_from_roman_to_arabic("XXX"))

    def test_that_converter_returns_2000_when_given_mm(self):
        self.assertEqual(2000, Converter.convert_from_roman_to_arabic("MM"))

if __name__ == '__main__':
    unittest.main()
