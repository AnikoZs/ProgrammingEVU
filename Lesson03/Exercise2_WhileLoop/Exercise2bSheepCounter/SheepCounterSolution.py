class SheepCounter:
    # Constructor
    def __init__(self, sheep):
        self.sheep = sheep
        self.max_sheep = 50

    # Task 1
    # Start counting at 3 instead of 1
    def count_from_three(self):
        i = 3

        while i <= self.sheep:
            print(f"Sheep number {i}")
            i += 1

        print("You fall asleep...")

    # Task 2
    # Stop counting at 50 sheep
    def count_to_fifty(self):
        i = 1

        while i <= 50:
            print(f"Sheep number {i}")
            i += 1

        print("You fall asleep...")

    # Task 3
    # Print only even sheep numbers
    def count_even_sheep(self):
        i = 1

        while i <= self.sheep:

            # Check if the number is even
            if i % 2 == 0:
                print(f"Sheep number {i}")

            i += 1

        print("You fall asleep...")

    # Task 4
    # Use the private variable max_sheep
    def count_using_max_sheep(self):
        i = 1

        while i <= self.max_sheep:
            print(f"Sheep number {i}")
            i += 1

        print("You fall asleep...")

    # Task 5
    # Count down instead of up
    def count_down(self):
        i = self.sheep

        while i >= 1:
            print(f"Sheep number {i}")
            i -= 1

        print("You fall asleep...")


class SheepCounterTest:

    @staticmethod
    def test():
        counter = SheepCounter(10)

        print("\n--- Task 1 Solution ---")
        counter.count_from_three()

        print("\n--- Task 2 Solution ---")
        counter.count_to_fifty()

        print("\n--- Task 3 Solution ---")
        counter.count_even_sheep()

        print("\n--- Task 4 Solution ---")
        counter.count_using_max_sheep()

        print("\n--- Task 5 Solution ---")
        counter.count_down()


# Start the program
SheepCounterTest.test()