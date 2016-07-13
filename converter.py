import numbers


class RomanNumeralConverter(object):

    arabic_lookup = {
        0: "",
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }

    roman_lookup = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # Using this value often, save as constant
    LARGEST_VALUE = max(arabic_lookup.iterkeys())

    @classmethod
    def convert_from_arabic_to_roman(cls, number):
        # Sanity checks
        try:
            int(number)
        except ValueError:
            raise ValueError("Tried to convert a non-number")
        if not isinstance(number, numbers.Integral):
            raise ValueError("Tried to convert a non-integer number")
        if number < 0:
            raise ValueError("Tried to convert a negative number")
        elif number > 3999:
            raise ValueError("Tried to convert a number larger than 3999")

        # Recursive call
        return cls.to_roman(number)

    @classmethod
    def to_roman(cls, number):
        # Track the largest symbol, add it on, then convert the rest
        last_step = cls.LARGEST_VALUE
        for step in sorted(cls.arabic_lookup.keys()):
            if number < step or number > cls.LARGEST_VALUE:
                return cls.arabic_lookup[last_step] + cls.convert_from_arabic_to_roman(number - last_step)
            elif number == step:
                return cls.arabic_lookup[step]
            last_step = step

    @classmethod
    def convert_from_roman_to_arabic(cls, number):

        if not all(symbol in cls.roman_lookup.keys() for symbol in number):
            raise ValueError("Tried to convert unrecognized symbol")

        # Base case
        if len(number) == 1:
            return cls.roman_lookup[number]

        if cls.roman_lookup[number[0]] < cls.roman_lookup[number[1]]:
            return cls.convert_from_roman_to_arabic(number[1:]) - cls.roman_lookup[number[0]]

        return cls.roman_lookup[number[0]] + cls.convert_from_roman_to_arabic(number[1:])
