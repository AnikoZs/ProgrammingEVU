class ZodiacSign:
    """
    ZodiacSign class
    Determines a zodiac sign based on the month and day of birth
    """

    def __init__(self, day, month):
        # Store the day and month
        self.day = day
        self.month = month

    # Return the zodiac sign
    def get_zodiac_sign(self):

        if (self.month == 3 and self.day >= 21) or (self.month == 4 and self.day <= 19):
            return "Aries"

        elif (self.month == 4 and self.day >= 20) or (self.month == 5 and self.day <= 20):
            return "Taurus"

        elif (self.month == 5 and self.day >= 21) or (self.month == 6 and self.day <= 20):
            return "Gemini"

        elif (self.month == 6 and self.day >= 21) or (self.month == 7 and self.day <= 22):
            return "Cancer"

        elif (self.month == 7 and self.day >= 23) or (self.month == 8 and self.day <= 22):
            return "Leo"

        elif (self.month == 8 and self.day >= 23) or (self.month == 9 and self.day <= 22):
            return "Virgo"

        elif (self.month == 9 and self.day >= 23) or (self.month == 10 and self.day <= 22):
            return "Libra"

        elif (self.month == 10 and self.day >= 23) or (self.month == 11 and self.day <= 21):
            return "Scorpio"

        elif (self.month == 11 and self.day >= 22) or (self.month == 12 and self.day <= 21):
            return "Sagittarius"

        elif (self.month == 12 and self.day >= 22) or (self.month == 1 and self.day <= 19):
            return "Capricorn"

        elif (self.month == 1 and self.day >= 20) or (self.month == 2 and self.day <= 18):
            return "Aquarius"

        elif (self.month == 2 and self.day >= 19) or (self.month == 3 and self.day <= 20):
            return "Pisces"

        else:
            return "Invalid date"