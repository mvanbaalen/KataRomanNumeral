class RomanNumeralConverter(object):

    lookup = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }

    @classmethod
    def convert_from_arabic_to_roman(cls, number):
        final_numeral = ""
        # Naively add Is to match the number
        if number < 4:
            for n in range(number):
                final_numeral += "I"
        else:
            return cls.lookup[number]
        return final_numeral
