class SheepCounter:
    # Constructor
    def __init__(self, sheep):
        self.sheep = sheep

    # Method that counts sheep
    def count_sheep(self):
        i = 1

        # Continue while i is less than or equal to sheep
        while i <= self.sheep:
            print(f"Sheep number {i}")

            # Move to the next sheep
            i += 1

        print("You fall asleep...")


class SheepCounterTest:

    @staticmethod
    def test():
        # Create a SheepCounter object
        counter = SheepCounter(5)

        # Start counting sheep
        counter.count_sheep()


# Start the program
SheepCounterTest.test()