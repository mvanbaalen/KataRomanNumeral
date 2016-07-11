import unittest
from converter import RomanNumeralConverter as Converter


class TestRequirements(unittest.TestCase):

    def test_that_tests_are_running(self):
        self.assertEqual(True, True)

    def test_that_converter_returns_i_when_given_1(self):
        self.assertEqual("I", Converter.convert_from_arabic_to_roman(1))

    def test_that_converter_returns_iii_when_given_3(self):
        self.assertEqual("III", Converter.convert_from_arabic_to_roman(3))

if __name__ == '__main__':
    unittest.main()