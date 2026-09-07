import random


class Coin:
    # Constructor
    def __init__(self):
        # Create a random number generator
        self.side = "Heads"  # Default value

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
        return f"Coin shows: {self.side}"


class CoinTest:

    @staticmethod
    def test():
        # Create a Coin object
        my_coin = Coin()

        # Flip the coin 5 times
        for i in range(1, 6):
            my_coin.flip()
            print(f"Flip {i}: {my_coin}")


# Start the program
CoinTest.test()