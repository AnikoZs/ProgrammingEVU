import random

from Lesson05.Exercise1_BattleShip.DotCom import DotCom


class GameLauncher:

    @staticmethod
    def main():

        # Create a DotCom object
        dot = DotCom()

        # Define the size of the game board
        grid_size = 7

        # Define the ship size
        ship_size = 3

        # Pick a random starting position
        # that allows the ship to fit on the board
        start = random.randint(0, grid_size - ship_size)

        # Create the ship locations
        locations = []

        for i in range(ship_size):
            locations.append(start + i)

        # Set the ship's location
        dot.set_location_cells(locations)

        print("🎯 Sink a Dot Com!")
        print("Grid positions are 0 to 6.")
        print("Try to sink the 3-cell ship.")

        # Count the number of guesses
        num_guesses = 0

        # Controls the game loop
        is_alive = True

        while is_alive:

            user_input = input("Enter a guess (0-6): ").strip()

            num_guesses += 1

            result = dot.check_yourself(user_input)

            print(result.upper())

            if result == "kill":
                print(f"You took {num_guesses} guesses. GG! 🚢💥")
                is_alive = False


if __name__ == "__main__":
    GameLauncher.main()