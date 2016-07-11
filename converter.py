class RomanNumeralConverter(object):
    @staticmethod
    def convert_from_arabic_to_roman(number):
        final_numeral = ""
        # Naively add Is to match the number
        for n in range(number):
            final_numeral += "I"
        return final_numeral
