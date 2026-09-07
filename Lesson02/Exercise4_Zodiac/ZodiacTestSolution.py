from Lesson02.Exercise4_Zodiac.ZodiacSign import ZodiacSign


class ZodiacTest:

    @staticmethod
    def main():

        # Print a title to the user
        print("Which zodiac sign are you?")

        # Ask the user to enter their birth day
        print("Enter your birth day: ", end="")

        # Read an integer from the keyboard and store it in the variable 'day'
        day = int(input())

        # Ask the user to enter their birth month
        print("Enter your birth month: ", end="")

        # Read an integer from the keyboard and store it in the variable 'month'
        month = int(input())

        # Create an object of the ZodiacSign class
        zodiac = ZodiacSign(day, month)

        # Call the get_zodiac_sign() method on the object
        # The method returns a string with the zodiac sign
        sign = zodiac.get_zodiac_sign()

        # Print the result to the user
        print("Your zodiac sign is:", sign)


# Start the program
if __name__ == "__main__":
    ZodiacTest.main()