import random


class Coin:
    # Constructor
    def __init__(self):
        self.side = "Heads"  # Default value

    # Flip the coin
    def flip(self):
        result = random.randint(0, 1)

        # Ternary operator
        self.side = "Heads" if result == 0 else "Tails"

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

        # Continue until we have 5 Heads
        while heads_count < 5:

            my_coin.flip()
            total_flips += 1

            print(f"Flip {total_flips}: {my_coin}")

            # Python equivalent of Java switch
            match my_coin.get_side():

                case "Heads":
                    heads_count += 1

                case "Tails":
                    tails_count += 1

                case _:
                    print("Unknown result!")

        # Print summary
        print("\nFinished!")
        print(f"Total flips: {total_flips}")
        print(f"Heads: {heads_count}")
        print(f"Tails: {tails_count}")


# Start the program
CoinTest.test()
