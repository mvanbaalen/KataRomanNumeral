import unittest
from converter import RomanNumeralConverter as Converter


class TestToArabicConversion(unittest.TestCase):

    def test_that_tests_are_running(self):
        self.assertEqual(True, True)

    def test_that_converter_returns_1_when_given_i(self):
        self.assertEqual(1, Converter.convert_from_roman_to_arabic("I"))

if __name__ == '__main__':
    unittest.main()
