import random


class Coin:
    # Constructor
    def __init__(self):
        self.side = "Heads"  # Default side

    # Flip the coin
    def flip(self):
        result = random.randint(0, 1)

        if result == 0:
            self.side = "Heads"
        else:
            self.side = "Tails"

    # Return the current side
    def get_side(self):
        return self.side

    # Define how the object is printed
    def __str__(self):
        return self.side


class CoinTest:

    @staticmethod
    def test():
        # Create a Coin object
        my_coin = Coin()

        # Counters for the results
        heads_count = 0
        tails_count = 0

        # Flip the coin 5 times
        for i in range(1, 6):
            my_coin.flip()

            print(f"Flip {i}: {my_coin}")

            # Count the results
            if my_coin.get_side() == "Heads":
                heads_count += 1
            else:
                tails_count += 1

        # Print summary
        print("\nSummary:")
        print(f"Heads: {heads_count}")
        print(f"Tails: {tails_count}")


# Start the program
CoinTest.test()