import random


class Coin:
    # Constructor
    def __init__(self):
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
        return self.side


class CoinTest:

    @staticmethod
    def test():
        # Create a Coin object
        my_coin = Coin()

        # Counters
        heads_count = 0
        tails_count = 0
        total_flips = 0

        # Keep flipping until we get 5 Heads
        while heads_count < 5:

            # Flip the coin
            my_coin.flip()

            # Count total flips
            total_flips += 1

            # Print the result
            print(f"Flip {total_flips}: {my_coin}")

            # Update counters
            if my_coin.get_side() == "Heads":
                heads_count += 1
            else:
                tails_count += 1

        # Print summary
        print("\nFinished!")
        print(f"Total flips: {total_flips}")
        print(f"Heads: {heads_count}")
        print(f"Tails: {tails_count}")


# Start the program
CoinTest.test()