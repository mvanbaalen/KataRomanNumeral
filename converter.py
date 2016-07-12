class RomanNumeralConverter(object):

    arabic_lookup = {
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

    # Using this value often, save as constant
    LARGEST_VALUE = max(arabic_lookup.iterkeys())

    @classmethod
    def convert_from_arabic_to_roman(cls, number):
        # Use recursion to add numbers together

        # Sanity check
        if number < 0:
            raise ValueError("Tried to convert a negative number")

        # Base case
        if number == 0:
            return ""

        # Track the largest symbol, add it on, then convert the rest
        last_step = cls.LARGEST_VALUE
        for step in sorted(cls.arabic_lookup.keys()):
            if number < step or number > cls.LARGEST_VALUE:
                return cls.arabic_lookup[last_step] + cls.convert_from_arabic_to_roman(number - last_step)
            elif number == step:
                return cls.arabic_lookup[step]
            last_step = step
