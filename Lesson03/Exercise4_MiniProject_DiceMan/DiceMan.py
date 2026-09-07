import random


class DiceMan:
    # Constructor
    def __init__(self, name):
        self.name = name
        self.number_of_activities = 0
        self.bed_count = 0

    # Roll a dice and return a number from 1 to 6
    def roll_dice(self):
        return random.randint(1, 6)

    # Perform an activity based on the dice roll
    def do_activity(self, roll):

        if roll == 1:
            print("Activity: Eat breakfast")

        elif roll == 2:
            print("Activity: Study something boring")

        elif roll == 3:
            print("Activity: Go swimming")

        elif roll == 4:
            print("Activity: Go fishing")

        elif roll == 5:
            print("Activity: Call his mom")

        elif roll == 6:
            print("Activity: Go back to bed")

            # Count how many times he goes back to bed
            self.bed_count += 1

    # Simulate the Dice Man's day
    def start_day(self):

        print(f"\nWelcome to {self.name}'s day!\n")

        while self.number_of_activities < 5:

            # Roll the dice
            roll = self.roll_dice()

            print(f"The Dice Man rolled: {roll}")

            # Perform the activity
            self.do_activity(roll)

            # Count completed activities
            self.number_of_activities += 1

            print()

            # Advanced Challenge
            if self.bed_count >= 3:
                print("The Dice Man got too lazy and stayed in bed forever...")
                return

        print("The Dice Man completed 5 activities today!")


class DiceManTest:

    @staticmethod
    def test():

        # Create a DiceMan object
        dice_man = DiceMan("Bob")

        # Start the day
        dice_man.start_day()


# Start the program
DiceManTest.test()