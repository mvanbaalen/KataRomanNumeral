import unittest
from converter import RomanNumeralConverter as Converter


class TestToRomanConversion(unittest.TestCase):

    def test_that_tests_are_running(self):
        self.assertEqual(True, True)

    def test_that_converter_handles_a_negative_number(self):
        self.assertRaises(ValueError, Converter.convert_from_arabic_to_roman, -5)

    def test_that_converter_handles_an_empty_value(self):
        self.assertRaises(ValueError, Converter.convert_from_arabic_to_roman, "")

    def test_that_converter_handles_a_string_value(self):
        self.assertRaises(ValueError, Converter.convert_from_arabic_to_roman, "one")

if __name__ == '__main__':
    unittest.main()