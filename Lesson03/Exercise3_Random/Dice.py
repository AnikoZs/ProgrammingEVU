import random


class Dice6:
    # Constructor
    def __init__(self):
        pass

    # Roll the dice until a 6 appears
    def roll_until_six(self):
        roll = 0

        while roll != 6:
            roll = random.randint(1, 6)
            print(f"Rolled: {roll}")

        print("Finally got a SIX!")


class Dice6Test:

    @staticmethod
    def test():
        # Create a Dice6 object
        dice = Dice6()

        # Start rolling
        dice.roll_until_six()


# Start the program
Dice6Test.test()